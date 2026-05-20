<div align="center">
  <img src="assets/speech-paper-wechat-hero.png" alt="Speech Paper WeChat pipeline illustration" width="100%" />

  <h1>📡 Speech Paper WeChat</h1>

  <p><strong>Agent-operated daily speech/audio paper digests for WeChat Official Accounts.</strong></p>

  <p>
    <a href="README.zh-CN.md">中文</a>
    · <a href="#agent-usage">Agent Usage</a>
    · <a href="#manual-usage">Manual Usage</a>
    · <a href="references/workflow.md">Workflow</a>
    · <a href="LICENSE">License</a>
  </p>

  <p>
    <img alt="GitHub Release" src="https://img.shields.io/badge/GitHub%20Release-v1.8.0-f97316?logo=github">
    <img alt="Platform" src="https://img.shields.io/badge/Platform-Codex%20%7C%20Claude%20Code%20%7C%20OpenClaw-111827?logo=openai">
    <img alt="Skill" src="https://img.shields.io/badge/Skill-SKILL.md-7c3aed?logo=markdown">
    <img alt="License" src="https://img.shields.io/badge/License-Apache--2.0-blue?logo=apache">
    <img alt="Python" src="https://img.shields.io/badge/Python-3.10%2B-3776ab?logo=python&logoColor=white">
    <img alt="arXiv" src="https://img.shields.io/badge/arXiv-cs.SD%20%7C%20eess.AS-b31b1b?logo=arxiv">
    <img alt="WeChat" src="https://img.shields.io/badge/WeChat-Official%20Account-07c160?logo=wechat&logoColor=white">
  </p>
</div>

Speech Paper WeChat is an end-to-end, agent-first pipeline for turning daily
speech and audio papers from arXiv into WeChat Official Account drafts.

The repository monitors the exact date blocks on arXiv `cs.SD` and `eess.AS`,
downloads candidate PDFs, extracts text, helps maintain structured paper reviews,
builds WeChat-ready Markdown, generates a content-aware cover image, and pushes
single or multi-article drafts to a WeChat Official Account.

If this project is useful to you, please consider giving it a star. It helps the
project reach more speech, audio, and research tooling developers.

## 📬 Follow the Daily Digest

<div align="center">
  <img src="assets/wechat-official-account-qr.png" alt="WeChat Official Account QR code" width="220" />
  <p><strong>Scan with WeChat</strong> to follow the Official Account powered by this pipeline.</p>
  <p>It publishes daily speech/audio paper digests generated with this skill.</p>
</div>

## 🗞️ News

- **2026-05-21**: Initial public repository structure for the daily speech paper
  WeChat pipeline.
- **2026-05-21**: Renamed the cover-image entry point to `nanobanana` and kept a
  legacy compatibility wrapper.
- **2026-05-20**: Validated the workflow on the arXiv `Wed, 20 May 2026` date
  blocks from `cs.SD` and `eess.AS`.

## ✨ Features

- **Agent-first operation**: designed for Codex, Claude Code, and OpenClaw-style
  coding agents that can follow `SKILL.md`.
- **Date-block collection**: collect papers from the exact arXiv recent-list
  date block.
- **Speech/audio scope**: track both `cs.SD` and `eess.AS`, with duplicate arXiv
  IDs merged.
- **PDF-grounded review**: download PDFs and extract first-page/full-text content
  with `pdftotext`.
- **Structured records**: build `reviewed.jsonl` / `reviewed.json` for
  review-driven article generation.
- **WeChat Markdown**: generate a featured article and a full daily roundup.
- **Cover generation**: create content-aware cover prompts and cover images
  through `nanobanana`.
- **Draft publishing**: publish WeChat drafts, including multi-article drafts via
  `--multi-manifest`.
- **Secret hygiene**: keep credentials out of version control through
  `.env.example` templates.

## 🧭 What It Automates

| Stage | Output |
| --- | --- |
| Paper collection | `metadata_today.json`, downloaded PDFs, extracted text |
| Agent review | `reviewed.jsonl`, `reviewed.json` |
| Article build | WeChat-ready Markdown and multi-article manifest |
| Cover design | Content-aware prompt and generated cover image |
| Publishing | WeChat Official Account draft box entry |

## 📁 Repository Layout

```text
speech-paper-wechat/
  README.md
  README.zh-CN.md
  LICENSE
  SKILL.md
  CHANGELOG.md
  assets/
    speech-paper-wechat-hero.png
    wechat-official-account-qr.png
  config/
    nanobanana.env.example
  references/
    workflow.md
  scripts/
    collect_arxiv_recent.py
    make_cover_prompt.py
    build_wechat_markdown.py
    image/
      generate_nanobanana.py
      generate_ikun.py        # legacy compatibility wrapper
    wechat/
      package.json
      wechat-api.ts
      wechat-extend-config.ts
      wechat-image-processor.ts
      md-to-wechat.ts
      .baoyu-skills/.env.example
      vendor/
```

## 🧰 Requirements

- Python 3.10+
- `pdftotext` for PDF text extraction
- Bun / Node.js for the WeChat publisher
- WeChat Official Account `AppID` and `AppSecret`
- Optional: `NANOBANANA_API_KEY` for cover image generation

On macOS, `pdftotext` is commonly provided by Poppler:

```bash
brew install poppler
```

Install the WeChat publisher dependencies:

```bash
cd scripts/wechat
npx -y bun install
```

## 🔐 Configuration

Copy the example files and fill them locally. Do not commit real credentials.

```bash
cp scripts/wechat/.baoyu-skills/.env.example scripts/wechat/.baoyu-skills/.env
cp config/nanobanana.env.example config/nanobanana.env
```

Expected WeChat variables:

```bash
WECHAT_APP_ID=
WECHAT_APP_SECRET=
```

Expected cover-image variable:

```bash
NANOBANANA_API_KEY=
```

`config/nanobanana.env`, `.env`, generated PDFs, images, and run outputs are
ignored by git.

<a id="agent-usage"></a>

## 🤖 Intended Usage: Codex / Claude Code

This repository is designed to be operated by coding agents such as **Codex** or
**Claude Code**. The scripts are exposed for reproducibility and debugging, but
the intended user experience is to ask an agent to run the daily workflow from
the repository root.

Open this repository in your agent environment, make sure credentials are
configured, and ask the agent to follow [SKILL.md](SKILL.md) plus
[references/workflow.md](references/workflow.md).

Example prompt:

```text
Use this repository's SKILL.md to generate the daily speech paper WeChat draft.
Target arXiv heading: "Wed, 20 May 2026".
Only read the cs.SD and eess.AS date blocks for that heading.
Ignore replacement entries.
Download PDFs, inspect the paper text, build reviewed.jsonl, generate the
WeChat Markdown, generate a nanobanana cover, and push a multi-article draft
after confirming every authors_org field is complete.
```

Draft-only prompt:

```text
Run the speech-paper-wechat pipeline for today's arXiv speech/audio papers.
Stop after generating reviewed.jsonl, reviewed.json, wechat-post.md, and the
cover image. Do not publish to WeChat.
```

Collection-only prompt:

```text
Collect the target arXiv date block for cs.SD and eess.AS, download PDFs, and
extract first-page/full-text files. Do not write reviews or publish.
```

The agent should handle the command sequence, intermediate files, validation,
and recovery. Manual commands below are mainly for debugging, CI, and custom
automation.

<a id="manual-usage"></a>

## 🛠️ Manual Usage

The example below reproduces the lower-level command sequence for the arXiv date
block `Wed, 20 May 2026`.

### 1. Collect Papers

```bash
python3 scripts/collect_arxiv_recent.py \
  --date-heading "Wed, 20 May 2026" \
  --output /tmp/papers_20260520 \
  --download-pdf \
  --extract-text
```

The collector writes:

```text
/tmp/papers_20260520/
  all_entries_today.json
  metadata_today.json
  pdf/
  firstpage/
  fulltext/
```

### 2. Prepare Structured Reviews

Create or update:

```text
/tmp/papers_20260520/reviewed.jsonl
```

Each line should be one reviewed paper record. The Markdown builder deduplicates
records by `arxiv_id` and keeps the latest record.

See [references/workflow.md](references/workflow.md) for the expected fields and
review rubric.

### 3. Build WeChat Markdown

```bash
python3 scripts/build_wechat_markdown.py \
  --input /tmp/papers_20260520/reviewed.jsonl \
  --output /tmp/papers_20260520/wechat-post.md \
  --date 2026-05-20
```

### 4. Generate a Cover Image

```bash
python3 scripts/make_cover_prompt.py \
  --input /tmp/papers_20260520/reviewed.jsonl \
  --output /tmp/papers_20260520/cover_prompt.txt

python3 scripts/image/generate_nanobanana.py \
  -p "$(cat /tmp/papers_20260520/cover_prompt.txt)" \
  -ar 21:9 \
  -s 2K \
  -o /tmp/papers_20260520/cover.png
```

### 5. Push a WeChat Draft

```bash
cd scripts/wechat
npx -y bun ./wechat-api.ts /tmp/papers_20260520/wechat-post.md \
  --author "JusperLee" \
  --cover /tmp/papers_20260520/cover.png \
  --multi-manifest /tmp/papers_20260520/wechat-post-multi.json
```

## 🔁 Daily Workflow

1. Choose the target arXiv date heading.
2. Run the collector for `cs.SD` and `eess.AS`.
3. Review each paper from the downloaded PDF text.
4. Append one JSON object per paper to `reviewed.jsonl`.
5. Build the featured and full-roundup WeChat Markdown.
6. Generate a content-aware cover image.
7. Push the final draft to the WeChat Official Account draft box.

The workflow intentionally ignores arXiv replacement blocks unless you explicitly
collect them outside this pipeline.

## 🛡️ Security

This repository does not contain real tokens, AppSecrets, API keys, PDFs, or
generated article outputs. Keep all production credentials in local ignored files
or environment variables.

Before publishing your fork, run:

```bash
rg --hidden --no-ignore "WECHAT_APP_SECRET|NANOBANANA_API_KEY|sk-" .
```

## 🗺️ Roadmap

- Add a one-command daily runner.
- Add schema validation for `reviewed.jsonl`.
- Add CI checks for Python scripts and Markdown examples.
- Add optional GitHub Actions templates for scheduled paper collection.

## 🤝 Contributing

Issues and pull requests are welcome. For larger changes, please open an issue
first to discuss the intended workflow impact.

## 📮 Contact

Maintainer: Kai Li  
Email: [thucs.kaili@gmail.com](mailto:thucs.kaili@gmail.com)

## 📜 License

This project is licensed under the [Apache License 2.0](LICENSE).
