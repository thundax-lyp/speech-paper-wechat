#!/usr/bin/env python3
"""Collect one date block from arXiv cs.AI/cs.CL/cs.MA recent pages.

This script intentionally keeps dependencies to the Python standard library.
It writes the same cache layout used by the Agent/LLM Paper WeChat workflow:

  all_entries_today.json
  metadata_today.json
  pdf/<arxiv_id>.pdf
  firstpage/<arxiv_id>.txt
  fulltext/<arxiv_id>.txt

PDF text extraction requires the external `pdftotext` binary.
"""

from __future__ import annotations

import argparse
import html
import http.client
import json
import re
import shutil
import subprocess
import time
import urllib.error
import urllib.request
from dataclasses import dataclass, asdict
from pathlib import Path


DEFAULT_CATEGORIES = ["cs.AI", "cs.CL", "cs.MA"]


def recent_url(category: str) -> str:
    return f"https://arxiv.org/list/{category}/recent?skip=0&show=2000"


AGENT_LLM_ANCHOR_KEYWORDS = [
    "agent", "agents", "agentic", "multi-agent", "multiagent",
    "large language model", "large language models", "llm", "llms",
    "language model", "foundation model", "chatbot", "assistant",
    "generative ai", "deep research", "web automation", "gui automation",
    "tool use", "tool-use", "function calling", "planning", "planner",
    "chain-of-thought", "cot", "self-reflection",
    "retrieval augmented", "retrieval-augmented", "rag", "memory",
    "prompt", "prompting", "instruction tuning",
]

AGENT_LLM_CONTEXT_KEYWORDS = [
    "reasoning", "planning", "planner", "alignment", "preference optimization",
    "rlhf", "dpo", "benchmark", "evaluation", "hallucination", "safety",
    "guardrail", "workflow", "orchestration", "tool", "retrieval",
]


@dataclass
class ArxivEntry:
    id: str
    source: str
    title: str
    authors: list[str]
    abstract: str
    comments: str
    subjects: str
    abs_url: str
    pdf_url: str
    html_url: str


def fetch_text(url: str, timeout: int) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "speech-paper-wechat/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        try:
            data = resp.read()
        except http.client.IncompleteRead as exc:
            data = exc.partial
        return data.decode("utf-8", errors="replace")


def strip_tags(value: str) -> str:
    value = re.sub(r"<script[\s\S]*?</script>", " ", value, flags=re.I)
    value = re.sub(r"<style[\s\S]*?</style>", " ", value, flags=re.I)
    value = re.sub(r"<[^>]+>", " ", value)
    return " ".join(html.unescape(value).split())


def extract_div(block: str, class_name: str) -> str:
    match = re.search(
        rf"<div[^>]*class=['\"][^'\"]*\b{re.escape(class_name)}\b[^'\"]*['\"][^>]*>(.*?)</div>",
        block,
        flags=re.S,
    )
    return match.group(1) if match else ""


def parse_entries(source: str, page_html: str, date_heading: str) -> list[ArxivEntry]:
    date_re = re.escape(date_heading)
    match = re.search(rf"<h3>\s*{date_re}.*?</h3>(.*?)(?=<h3>|\Z)", page_html, re.S)
    if not match:
        return []

    entries: list[ArxivEntry] = []
    for raw in re.split(r"<dt>", match.group(1))[1:]:
        raw = raw.split("</dd>", 1)[0]
        id_match = re.search(r"arXiv:([0-9]{4}\.[0-9]+)", raw)
        if not id_match:
            continue
        arxiv_id = id_match.group(1)
        title = strip_tags(extract_div(raw, "list-title")).removeprefix("Title:").strip()
        abstract = strip_tags(extract_div(raw, "list-abstract"))
        abstract = abstract.replace("▽ More", "").replace("△ Less", "").strip()
        comments = strip_tags(extract_div(raw, "list-comments")).removeprefix("Comments:").strip()
        subjects = strip_tags(extract_div(raw, "list-subjects")).removeprefix("Subjects:").strip()

        authors_html = extract_div(raw, "list-authors")
        authors = [
            strip_tags(author)
            for author in re.findall(r"<a[^>]*>(.*?)</a>", authors_html, flags=re.S)
        ]

        entries.append(
            ArxivEntry(
                id=arxiv_id,
                source=source,
                title=title,
                authors=authors,
                abstract=abstract,
                comments=comments,
                subjects=subjects,
                abs_url=f"https://arxiv.org/abs/{arxiv_id}",
                pdf_url=f"https://arxiv.org/pdf/{arxiv_id}",
                html_url=f"https://arxiv.org/html/{arxiv_id}",
            )
        )
    return entries


def unique_entries(entries: list[ArxivEntry]) -> list[dict]:
    by_id: dict[str, dict] = {}
    for entry in entries:
        item = asdict(entry)
        if entry.id not in by_id:
            item["sources"] = [entry.source]
            by_id[entry.id] = item
        else:
            by_id[entry.id]["sources"].append(entry.source)
            if not by_id[entry.id].get("abstract") and entry.abstract:
                by_id[entry.id]["abstract"] = entry.abstract
    return list(by_id.values())


def matches_agent_llm(item: dict) -> tuple[bool, list[str]]:
    haystack = " ".join(
        str(item.get(key, "") or "")
        for key in ("title", "abstract", "subjects", "comments")
    ).lower()
    anchors = [kw for kw in AGENT_LLM_ANCHOR_KEYWORDS if kw in haystack]
    contexts = [kw for kw in AGENT_LLM_CONTEXT_KEYWORDS if kw in haystack]
    if anchors:
        return True, (anchors + contexts)[:8]
    # Keep a small number of clearly LLM-coded alignment/safety acronyms even
    # when the title omits "LLM".
    strong_contexts = [kw for kw in contexts if kw in {"rlhf", "dpo", "preference optimization", "hallucination", "guardrail"}]
    return bool(strong_contexts), (strong_contexts + contexts)[:8]


def download(url: str, output: Path, timeout: int, retries: int = 3) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = output.with_suffix(output.suffix + ".tmp")
    if shutil.which("curl"):
        result = subprocess.run(
            [
                "curl",
                "-L",
                "--fail",
                "--retry",
                str(retries),
                "--retry-delay",
                "2",
                "--max-time",
                str(timeout),
                "-A",
                "speech-paper-wechat/1.0",
                "-o",
                str(tmp_path),
                url,
            ],
            check=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        if result.returncode == 0 and tmp_path.exists() and tmp_path.stat().st_size > 0:
            tmp_path.replace(output)
            return
        if tmp_path.exists():
            tmp_path.unlink()

    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        req = urllib.request.Request(url, headers={"User-Agent": "speech-paper-wechat/1.0"})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                data = resp.read()
            tmp_path.write_bytes(data)
            tmp_path.replace(output)
            return
        except (http.client.IncompleteRead, TimeoutError, urllib.error.URLError) as exc:
            last_error = exc
            if tmp_path.exists():
                tmp_path.unlink()
            if attempt < retries:
                time.sleep(attempt)
    if last_error:
        raise last_error


def extract_pdf_text(pdf_path: Path, firstpage_path: Path, fulltext_path: Path) -> None:
    firstpage_path.parent.mkdir(parents=True, exist_ok=True)
    fulltext_path.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["pdftotext", "-f", "1", "-l", "2", "-layout", str(pdf_path), str(firstpage_path)],
        check=False,
    )
    subprocess.run(["pdftotext", "-layout", str(pdf_path), str(fulltext_path)], check=False)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date-heading", required=True, help='arXiv heading, e.g. "Wed, 20 May 2026"')
    parser.add_argument("--output", required=True, type=Path, help="Run cache directory")
    parser.add_argument(
        "--categories",
        nargs="+",
        default=DEFAULT_CATEGORIES,
        help="arXiv categories to collect, e.g. cs.AI cs.CL cs.MA",
    )
    parser.add_argument(
        "--filter-profile",
        choices=["agent-llm", "none"],
        default="agent-llm",
        help="Filter collected metadata before downloading PDFs",
    )
    parser.add_argument("--download-pdf", action="store_true", help="Download unique PDFs")
    parser.add_argument("--extract-text", action="store_true", help="Run pdftotext after PDF download")
    parser.add_argument("--timeout", type=int, default=60)
    args = parser.parse_args()

    args.output.mkdir(parents=True, exist_ok=True)
    all_entries: list[ArxivEntry] = []
    for source in args.categories:
        page = fetch_text(recent_url(source), args.timeout)
        (args.output / f"{source}.recent.html").write_text(page, encoding="utf-8")
        all_entries.extend(parse_entries(source, page, args.date_heading))

    raw_json = [asdict(entry) for entry in all_entries]
    unfiltered_metadata = unique_entries(all_entries)
    metadata = unfiltered_metadata
    filter_report = {
        "profile": args.filter_profile,
        "input_count": len(unfiltered_metadata),
        "kept_count": len(unfiltered_metadata),
        "dropped_count": 0,
        "kept": [],
        "dropped": [],
    }
    if args.filter_profile == "agent-llm":
        kept = []
        dropped = []
        for item in unfiltered_metadata:
            ok, matched = matches_agent_llm(item)
            row = {
                "id": item.get("id"),
                "title": item.get("title"),
                "sources": item.get("sources", []),
                "matched_keywords": matched,
            }
            if ok:
                kept.append(item)
                filter_report["kept"].append(row)
            else:
                dropped.append(item)
                filter_report["dropped"].append(row)
        metadata = kept
        filter_report["kept_count"] = len(kept)
        filter_report["dropped_count"] = len(dropped)

    (args.output / "all_entries_today.json").write_text(
        json.dumps(raw_json, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (args.output / "metadata_unfiltered.json").write_text(
        json.dumps(unfiltered_metadata, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (args.output / "metadata_today.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (args.output / "filter_report.json").write_text(
        json.dumps(filter_report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    if args.download_pdf:
        for item in metadata:
            arxiv_id = item["id"]
            pdf_path = args.output / "pdf" / f"{arxiv_id}.pdf"
            if not pdf_path.exists() or pdf_path.stat().st_size == 0:
                download(item["pdf_url"], pdf_path, args.timeout)
            if args.extract_text:
                extract_pdf_text(
                    pdf_path,
                    args.output / "firstpage" / f"{arxiv_id}.txt",
                    args.output / "fulltext" / f"{arxiv_id}.txt",
                )

    duplicate_count = len(raw_json) - len(unfiltered_metadata)
    print(json.dumps({
        "raw_entries": len(raw_json),
        "unique_entries": len(metadata),
        "unique_entries_before_filter": len(unfiltered_metadata),
        "duplicates": duplicate_count,
        "filter_profile": args.filter_profile,
        "dropped_by_filter": filter_report["dropped_count"],
        "output": str(args.output),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
