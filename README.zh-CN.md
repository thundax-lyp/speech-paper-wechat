<div align="center">
  <img src="assets/speech-paper-wechat-hero.png" alt="Agent/LLM Paper WeChat pipeline illustration" width="100%" />

  <h1>📡 Agent/LLM Paper WeChat</h1>

  <p><strong>面向 Codex / Claude Code 的每日 Agent/LLM 论文微信公众号自动化 pipeline。</strong></p>

  <p>
    <a href="README.md">English</a>
    · <a href="#agent-usage">Agent 使用</a>
    · <a href="#manual-usage">手动调试</a>
    · <a href="references/workflow.md">Workflow</a>
    · <a href="LICENSE">License</a>
  </p>

  <p>
    <img alt="GitHub Release" src="https://img.shields.io/badge/GitHub%20Release-v1.8.0-f97316?logo=github">
    <img alt="Platform" src="https://img.shields.io/badge/Platform-Codex%20%7C%20Claude%20Code%20%7C%20OpenClaw-111827?logo=openai">
    <img alt="Skill" src="https://img.shields.io/badge/Skill-SKILL.md-7c3aed?logo=markdown">
    <img alt="License" src="https://img.shields.io/badge/License-Apache--2.0-blue?logo=apache">
    <img alt="Python" src="https://img.shields.io/badge/Python-3.10%2B-3776ab?logo=python&logoColor=white">
    <img alt="arXiv" src="https://img.shields.io/badge/arXiv-cs.AI%20%7C%20cs.CL%20%7C%20cs.MA-b31b1b?logo=arxiv">
    <img alt="WeChat" src="https://img.shields.io/badge/WeChat-Official%20Account-07c160?logo=wechat&logoColor=white">
  </p>
</div>

Agent/LLM Paper WeChat 是一个 agent-first 的端到端 pipeline，用于把每日 Agent / LLM 方向 arXiv 论文整理成微信公众号草稿。

本仓库会从 arXiv `cs.AI`、`cs.CL` 与 `cs.MA` 的 recent 页面中读取指定日期块，先按 Agent / LLM 相关性过滤，再下载候选论文 PDF，抽取文本，维护结构化评审记录，生成微信公众号 Markdown，自动生成内容感知封面，并推送到微信公众号草稿箱。

如果这个项目对你有帮助，欢迎点一个 Star。它会帮助项目被更多 Agent、LLM 和科研工具开发者看到。

## 📬 关注每日推送

<div align="center">
  <img src="assets/wechat-official-account-qr.png" alt="微信公众号二维码" width="220" />
  <p><strong>微信扫码关注</strong>这个 pipeline 每日推送的公众号。</p>
  <p>这里会发布由本 skill 生成的每日 Agent/LLM 论文速递。</p>
</div>

## 🗞️ News

- **2026-05-21**：整理为公开仓库结构，包含每日 Agent/LLM 论文公众号完整流程。
- **2026-05-21**：默认封面生成切换为 Codex 内置图片能力，保留旧命令兼容 wrapper。
- **2026-05-20**：已在 arXiv `Wed, 20 May 2026` 的 `cs.AI`、`cs.CL` 与 `cs.MA` 日期块上验证流程。

## ✨ 功能

- **Agent-first**：面向 Codex、Claude Code 和 OpenClaw 风格 coding agent，核心说明写在 `SKILL.md`。
- **日期块抓取**：只抓取 arXiv recent 页面中的目标日期块。
- **Agent/LLM 范围**：覆盖 `cs.AI`、`cs.CL` 和 `cs.MA`，并按 arXiv ID 合并重复论文。
- **下载前过滤**：先用 recent 页面元数据筛出 Agent / LLM 相关论文，再下载 PDF。
- **PDF-grounded review**：下载 PDF，并用 `pdftotext` 抽取首页与全文文本。
- **结构化记录**：通过 `reviewed.jsonl` / `reviewed.json` 维护逐篇结构化评审。
- **微信公众号 Markdown**：支持精选版与全量版。
- **封面生成**：通过 Codex 内置图片能力生成内容感知封面图。
- **草稿发布**：支持使用 `--multi-manifest` 推送多图文草稿。
- **敏感信息隔离**：所有敏感配置只保留模板，不提交真实凭据。

## 🧭 自动化内容

| 阶段 | 输出 |
| --- | --- |
| 论文抓取 | `metadata_unfiltered.json`、`metadata_today.json`、`filter_report.json`、PDF、抽取文本 |
| Agent 精读 | `reviewed.jsonl`、`reviewed.json` |
| 文章生成 | 微信公众号 Markdown 和多图文 manifest |
| 封面设计 | 内容感知 prompt 和封面图 |
| 发布 | 微信公众号草稿箱条目 |

## 📁 目录结构

```text
speech-paper-wechat/
  README.md
  README.zh-CN.md
  LICENSE
  SKILL.md
  assets/
    speech-paper-wechat-hero.png
    wechat-official-account-qr.png
  references/
    workflow.md
  scripts/
    collect_arxiv_recent.py
    make_cover_prompt.py
    build_wechat_markdown.py
    image/
      generate_codex_cover.py
      generate_nanobanana.py
      generate_ikun.py        # 旧入口兼容 wrapper
    wechat/
      package.json
      wechat-api.ts
      wechat-extend-config.ts
      wechat-image-processor.ts
      md-to-wechat.ts
      .baoyu-skills/.env.example
      vendor/
```

## 🧰 环境要求

- Python 3.10+
- `pdftotext`，用于 PDF 文本抽取
- Bun / Node.js，用于微信公众号发布脚本
- 微信公众号 `AppID` 与 `AppSecret`
- Codex 内置图片生成能力，用于封面图生成

macOS 可通过 Poppler 安装 `pdftotext`：

```bash
brew install poppler
```

安装微信公众号发布依赖：

```bash
cd scripts/wechat
npx -y bun install
```

## 🔐 配置

复制模板，并只在本地填写真实值。不要提交真实凭据。

```bash
cp scripts/wechat/.baoyu-skills/.env.example scripts/wechat/.baoyu-skills/.env
```

微信公众号配置：

```bash
WECHAT_APP_ID=
WECHAT_APP_SECRET=
```

封面图默认由 Codex agent 的内置图片能力生成，不需要额外图片 API Key。

`.env`、PDF、图片和较大的运行产物都已被 git 忽略。`runs/` 下最终生成的 WeChat Markdown 草稿和 `wechat-post-multi.json` 可以提交，用于审阅和留档。

<a id="agent-usage"></a>

## 🤖 推荐使用方式：Codex / Claude Code

这个仓库更适合由 **Codex** 或 **Claude Code** 这类 coding agent 直接操作。脚本是为了可复现、可调试和方便二次开发保留下来的，但正常使用时不需要用户一步一步手动执行。

在 agent 环境中打开本仓库，确认凭据已经配置好，然后让 agent 读取 [SKILL.md](SKILL.md) 和 [references/workflow.md](references/workflow.md) 执行任务即可。

示例 prompt：

```text
使用本仓库的 SKILL.md 生成每日 Agent/LLM 论文微信公众号草稿。
目标 arXiv 日期标题是："Wed, 20 May 2026"。
只读取 cs.AI、cs.CL 和 cs.MA 中这个日期块的论文。
忽略 replacement entries。
下载 PDF，阅读论文文本，生成 reviewed.jsonl，生成微信公众号 Markdown，
用 Codex 内置图片能力生成封面，并在确认所有 authors_org 都完整后推送多图文草稿。
```

只生成草稿、不发布：

```text
运行 agent-llm-paper-wechat pipeline，处理今天 arXiv 的 Agent/LLM 论文。
生成 reviewed.jsonl、reviewed.json、wechat-post.md 和封面图后停止。
不要推送到微信公众号。
```

只抓取论文：

```text
抓取 cs.AI、cs.CL 和 cs.MA 的目标 arXiv 日期块，先过滤 Agent / LLM 相关论文，再下载 PDF 并抽取首页和全文文本。
不要写评审，不要发布。
```

agent 应该负责执行命令、检查中间产物、处理失败和恢复流程。下面的手动命令主要用于调试、CI 或自定义自动化。

<a id="manual-usage"></a>

## 🛠️ 手动使用

下面示例展示底层命令序列，使用 arXiv 日期块 `Wed, 20 May 2026`。

### 1. 抓取论文

```bash
python3 scripts/collect_arxiv_recent.py \
  --date-heading "Wed, 20 May 2026" \
  --output runs/papers_20260520 \
  --categories cs.AI cs.CL cs.MA \
  --filter-profile agent-llm \
  --download-pdf \
  --extract-text
```

输出目录：

```text
runs/papers_20260520/
  all_entries_today.json
  metadata_unfiltered.json
  metadata_today.json
  filter_report.json
  pdf/
  firstpage/
  fulltext/
```

### 2. 维护结构化评审

创建或更新：

```text
runs/papers_20260520/reviewed.jsonl
```

每一行是一篇论文的结构化记录。Markdown 生成脚本会按 `arxiv_id` 去重，并保留同一论文的最新记录。

字段规范和评分口径见 [references/workflow.md](references/workflow.md)。

### 3. 生成微信公众号 Markdown

```bash
python3 scripts/build_wechat_markdown.py \
  --input runs/papers_20260520/reviewed.jsonl \
  --output runs/papers_20260520/wechat-post.md \
  --date 2026-05-20
```

### 4. 生成封面

```bash
python3 scripts/make_cover_prompt.py \
  --input runs/papers_20260520/reviewed.jsonl \
  --output runs/papers_20260520/cover_prompt.txt

python3 scripts/image/generate_codex_cover.py \
  --prompt-file runs/papers_20260520/cover_prompt.txt \
  -ar 21:9 \
  -s 2K \
  -o runs/papers_20260520/cover.png
```

上面的命令会生成 `runs/papers_20260520/cover.codex-image-request.md`。
在 Codex 中继续让 agent 使用内置图片能力按该请求出图，并把最终图片保存到
`runs/papers_20260520/cover.png`。

### 5. 推送微信公众号草稿

```bash
cd scripts/wechat
npx -y bun ./wechat-api.ts ../../runs/papers_20260520/wechat-post.md \
  --author "Thundax" \
  --cover ../../runs/papers_20260520/cover.png \
  --multi-manifest ../../runs/papers_20260520/wechat-post-multi.json
```

## 🔁 日常流程

1. 确认目标 arXiv 日期标题。
2. 抓取 `cs.AI`、`cs.CL` 与 `cs.MA`。
3. 基于下载后的 PDF 文本逐篇阅读和筛选。
4. 每篇论文向 `reviewed.jsonl` 追加一个 JSON 对象。
5. 生成精选版和全量版微信公众号 Markdown。
6. 生成内容感知封面图。
7. 推送到微信公众号草稿箱。

默认不处理 arXiv replacement block。

## 🛡️ 安全说明

仓库不包含真实 token、AppSecret、API key、PDF、封面图或全文抽取产物。最终 WeChat Markdown 草稿和 `wechat-post-multi.json` 可在审阅后提交。生产凭据请只放在本地 ignored 文件或环境变量中。

发布 fork 前建议运行：

```bash
rg --hidden --no-ignore "WECHAT_APP_SECRET|sk-" .
```

## 🗺️ Roadmap

- 增加一键运行每日任务的 runner。
- 增加 `reviewed.jsonl` schema 校验。
- 增加 Python 脚本和 Markdown 示例的 CI 检查。
- 增加可选的 GitHub Actions 定时抓取模板。

## 🤝 贡献

欢迎提交 issue 和 pull request。较大的流程改动建议先开 issue 讨论。

## 📮 联系方式

Maintainer: Kai Li  
Email: [thucs.kaili@gmail.com](mailto:thucs.kaili@gmail.com)

## 📜 License

本项目基于 [Apache License 2.0](LICENSE) 开源。
