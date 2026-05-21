# Repository Guidelines

## Project Structure & Module Organization

This repository is an agent-operated pipeline for turning daily arXiv Agent/LLM papers into WeChat Official Account drafts.

- `scripts/collect_arxiv_recent.py`: collects `cs.AI`, `cs.CL`, and `cs.MA` arXiv date blocks, filters Agent/LLM candidates, downloads PDFs, and extracts text.
- `scripts/build_wechat_markdown.py`: builds featured and full WeChat Markdown posts from `reviewed.jsonl`.
- `scripts/make_cover_prompt.py`: creates a content-aware cover prompt from reviewed papers.
- `scripts/image/`: cover-image request helpers; default flow uses Codex built-in image generation via `generate_codex_cover.py`.
- `scripts/wechat/`: Bun/TypeScript WeChat publisher and vendored markdown/CDP helpers.
- `references/workflow.md` and `SKILL.md`: canonical workflow and agent instructions.
- `assets/`: committed README images. Runtime outputs belong in `runs/papers_YYYYMMDD/`, which is ignored by git.

## Build, Test, and Development Commands

Install WeChat publisher dependencies:

```bash
cd scripts/wechat
PATH="$HOME/.bun/bin:$PATH" bun install
```

Collect papers for a date block:

```bash
python3 scripts/collect_arxiv_recent.py \
  --date-heading "Wed, 20 May 2026" \
  --output runs/papers_20260520 \
  --download-pdf --extract-text
```

Build article outputs:

```bash
python3 scripts/build_wechat_markdown.py \
  --input runs/papers_20260520/reviewed.jsonl \
  --output runs/papers_20260520/wechat-post.md \
  --date 2026-05-20
```

Run a lightweight syntax check:

```bash
python3 -m py_compile scripts/*.py scripts/image/*.py
```

## Coding Style & Naming Conventions

Use Python 3.10+ with standard-library tools unless a dependency already exists. Keep scripts CLI-friendly with `argparse`, explicit paths, and JSON/JSONL for structured data. Use snake_case for Python functions and filenames. TypeScript files in `scripts/wechat/` use ESM style and descriptive camelCase identifiers.

## Testing Guidelines

There is no formal test suite yet. Before changes, run `py_compile` for Python and a focused command that exercises the touched path. For publisher changes, run `bun install` and prefer dry validation of input files before calling WeChat APIs.

## Commit & Pull Request Guidelines

History is minimal, so use concise imperative commits such as `Add Codex cover helper` or `Update workflow paths`. PRs should explain the workflow impact, list commands run, mention generated files, and call out any publishing or credential-sensitive behavior.

## Security & Configuration Tips

Do not commit credentials or run outputs. Keep WeChat secrets in `scripts/wechat/.baoyu-skills/.env`. Keep PDFs, generated covers, `reviewed.jsonl`, and WeChat drafts under `runs/`. Before sharing, scan for secrets:

```bash
rg --hidden --no-ignore "WECHAT_APP_SECRET|sk-" .
```
