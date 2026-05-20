#!/usr/bin/env python3
"""Collect one date block from arXiv cs.SD/eess.AS recent pages.

This script intentionally keeps dependencies to the Python standard library.
It writes the same cache layout used by the speech-paper-wechat workflow:

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
import json
import re
import subprocess
import urllib.request
from dataclasses import dataclass, asdict
from pathlib import Path


RECENT_URLS = {
    "cs.SD": "https://arxiv.org/list/cs.SD/recent",
    "eess.AS": "https://arxiv.org/list/eess.AS/recent",
}


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
        return resp.read().decode("utf-8", errors="replace")


def strip_tags(value: str) -> str:
    value = re.sub(r"<script[\s\S]*?</script>", " ", value, flags=re.I)
    value = re.sub(r"<style[\s\S]*?</style>", " ", value, flags=re.I)
    value = re.sub(r"<[^>]+>", " ", value)
    return " ".join(html.unescape(value).split())


def extract_div(block: str, class_name: str) -> str:
    match = re.search(
        rf'<div class="{re.escape(class_name)}"[^>]*>(.*?)</div>',
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


def download(url: str, output: Path, timeout: int) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": "speech-paper-wechat/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        output.write_bytes(resp.read())


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
    parser.add_argument("--download-pdf", action="store_true", help="Download unique PDFs")
    parser.add_argument("--extract-text", action="store_true", help="Run pdftotext after PDF download")
    parser.add_argument("--timeout", type=int, default=60)
    args = parser.parse_args()

    args.output.mkdir(parents=True, exist_ok=True)
    all_entries: list[ArxivEntry] = []
    for source, url in RECENT_URLS.items():
        page = fetch_text(url, args.timeout)
        (args.output / f"{source}.recent.html").write_text(page, encoding="utf-8")
        all_entries.extend(parse_entries(source, page, args.date_heading))

    raw_json = [asdict(entry) for entry in all_entries]
    metadata = unique_entries(all_entries)
    (args.output / "all_entries_today.json").write_text(
        json.dumps(raw_json, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (args.output / "metadata_today.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
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

    duplicate_count = len(raw_json) - len(metadata)
    print(json.dumps({
        "raw_entries": len(raw_json),
        "unique_entries": len(metadata),
        "duplicates": duplicate_count,
        "output": str(args.output),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
