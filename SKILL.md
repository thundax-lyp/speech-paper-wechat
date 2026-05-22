---
name: speech-paper-wechat
description: "每日 Agent/LLM 论文速递-公众号版。搜索当天 arXiv cs.AI、cs.CL、cs.MA 新论文，先基于 recent 页面元数据过滤 Agent/LLM 相关论文，再下载候选 PDF 到项目 runs/ 目录，逐篇阅读 PDF/首页文本并把分类、作者机构、评分和评语追加写入 JSONL，最后生成 reviewed.json、精选版和全量版公众号草稿；使用固定 Agent/LLM taxonomy、方向/序号/论文/评分/关键词总览表、emoji 小标题和内容感知封面图，并通过仓库内置微信发布脚本推送为同一个多图文草稿。"
version: 2.0.0
author: Thundax
license: Apache-2.0
compatibility:
  platforms:
    - openclaw
metadata:
  openclaw:
    emoji: "📡"
    requires:
      bins: ["python3", "pdftotext", "bun"]
      skills: ["imagegen"]
---

# 每日 Agent/LLM 论文速递 — 公众号版

从 arXiv `cs.AI` / `cs.CL` / `cs.MA` 的目标日期块抓取论文 → 在下载 PDF 前过滤 Agent/LLM 相关论文 → 下载 PDF 与抽取文本 → 逐篇读论文并追加 JSONL → 生成公众号 markdown（精选版 + 全量版）→ 用 Codex 内置图片能力生成封面 → 推送草稿箱。

## 什么时候用

当用户有以下意图时触发：

- “生成今天的 Agent/LLM 论文公众号草稿”
- “把今天的 Agent 论文速递推到草稿箱”
- “抓取 cs.AI、cs.CL、cs.MA 里 Agent/LLM 相关论文”
- “跑每日 Agent/LLM 论文公众号”

## 路径与脚本

- 仓库根目录：`speech-paper-wechat`
- 运行产物：`$REPO_ROOT/runs/papers_YYYYMMDD/`
- 抓取脚本：`$REPO_ROOT/scripts/collect_arxiv_recent.py`
- Markdown 生成脚本：`$REPO_ROOT/scripts/build_wechat_markdown.py`
- 封面 prompt 脚本：`$REPO_ROOT/scripts/make_cover_prompt.py`
- 封面请求脚本：`$REPO_ROOT/scripts/image/generate_codex_cover.py`
- 微信发布目录：`$REPO_ROOT/scripts/wechat`
- 微信凭据：`$REPO_ROOT/scripts/wechat/.baoyu-skills/.env`，不要提交

## 日期选择硬规则

用户说“今天”“每日”“论文速递”或没有显式指定日期时，默认目标日期必须是当前运行日期，不允许因为本地已有旧产物而自动使用最近一期。

执行前必须先确定并记录：

- 当前日期：用运行环境的当前日期，格式为 `YYYY-MM-DD`
- arXiv 日期标题：把当前日期转换为 recent 页面使用的英文标题，例如 `Fri, 22 May 2026`
- 输出目录：必须与当前日期一致，例如 `runs/papers_20260522/`

在抓取前必须确认 `cs.AI`、`cs.CL`、`cs.MA` 的 recent 页面是否包含目标 arXiv 日期标题。若目标日期块尚未出现，必须停止并明确告诉用户：`YYYY-MM-DD` 的 arXiv 日期块暂未发布。禁止静默回退到前一天或复用 `runs/papers_YYYYMMDD/` 旧目录；只有用户明确同意“用最近一期/用昨天”后，才可以改用其他日期。

推送前还必须复核 `wechat-post-multi.json`、markdown frontmatter、文章标题和输出目录里的日期都等于目标日期。日期不一致时禁止推送草稿。

## 固化执行顺序

### 1) 抓取、过滤、下载

```bash
REPO_ROOT="/path/to/speech-paper-wechat"
TARGET_DATE="2026-05-22"
ARXIV_DATE_HEADING="Fri, 22 May 2026"
RUN_DIR="$REPO_ROOT/runs/papers_20260522"

python3 "$REPO_ROOT/scripts/collect_arxiv_recent.py" \
  --date-heading "$ARXIV_DATE_HEADING" \
  --output "$RUN_DIR" \
  --categories cs.AI cs.CL cs.MA \
  --filter-profile agent-llm \
  --download-pdf \
  --extract-text
```

强约束：先解析 recent 页面元数据，再按 Agent/LLM 关键词过滤，只下载过滤后 `metadata_today.json` 中的论文 PDF。保留 `metadata_unfiltered.json` 和 `filter_report.json` 便于复查误杀。

### 2) 逐篇阅读并写 JSONL

每篇保留论文都要读 PDF 首页；重要论文尽量读全文。不要只看 abstract 批量写结论。

每条 JSONL 至少包含：

- `arxiv_id`
- `kept`
- `title`
- `direction`
- `score`
- `novelty_score`
- `impact_score`
- `evidence_score`
- `audience_fit_score`
- `authors_org`
- `abs_url`
- `pdf_url`
- `code_url`
- `summary`
- `review`
- `architecture`
- `innovation`
- `training`
- `results`
- `why`

## Agent/LLM 过滤范围

保留：

- autonomous / embodied / web / coding / research agents
- tool use、function calling、workflow orchestration、memory
- LLM reasoning、planning、reflection、RAG、long-context
- multi-agent collaboration、negotiation、simulation、communication
- LLM alignment、preference optimization、safety、guardrails
- Agent/LLM evaluation、benchmarks、hallucination、reliability
- LLM applications with clear agentic behavior or strong model-method relevance

剔除：

- 纯 CV、机器人控制、图学习、优化、博弈论、社科仿真，且没有 LLM/Agent 方法连接
- 只有普通 NLP 分类/抽取任务，未涉及 LLM、agent、tool use、reasoning 或 RAG
- 与 Agent/LLM 只是营销式沾边、技术贡献不相关的论文

## 固定 Taxonomy

`direction` 只能从下面选择：

- `Agent系统与工具使用`
- `LLM推理与规划`
- `RAG与知识检索`
- `多智能体与协作`
- `LLM训练与对齐`
- `评测与安全`
- `应用与基准`
- `其他 Agent / LLM 方向`

## 评分口径

默认按 ML / NLP 顶会审稿口径打分：

- **新意（0–3）**：是否有清楚的新问题、新方法或新系统范式
- **影响力（0–3）**：是否触及 Agent/LLM 主线，而非特别窄的小修小补
- **证据强度（0–2）**：实验、消融、失败分析和对比是否站得住
- **受众匹配度（0–2）**：是否适合关注 Agent、LLM、RAG、对齐、评测的读者

`7` 以上才进精选；高分要克制，不要因为“用了 LLM”就加分。

## 生成 Markdown

```bash
python3 "$REPO_ROOT/scripts/build_wechat_markdown.py" \
  --input "$RUN_DIR/reviewed.jsonl" \
  --output "$RUN_DIR/wechat-post.md" \
  --date "$TARGET_DATE"
```

输出：

- `wechat-post.md`：精选版
- `wechat-post-all.md`：全量版
- `wechat-post-multi.json`：多图文 manifest

文章标题固定为：

- `Agent/LLM论文速递｜YYYY-MM-DD｜精选版`
- `Agent/LLM论文速递｜YYYY-MM-DD｜全量版`

## 封面生成

先生成 prompt 和 Codex 图片请求：

```bash
python3 "$REPO_ROOT/scripts/make_cover_prompt.py" \
  --input "$RUN_DIR/reviewed.jsonl" \
  --output "$RUN_DIR/cover_prompt.txt"

python3 "$REPO_ROOT/scripts/image/generate_codex_cover.py" \
  --prompt-file "$RUN_DIR/cover_prompt.txt" \
  -ar 21:9 \
  -s 2K \
  -o "$RUN_DIR/cover.png"
```

然后使用 Codex 内置图片能力生成封面，保存到 `cover.png`。视觉风格：现代 AI research newsletter 封面，体现智能体网络、工具调用、推理路径、记忆检索、多智能体协作和评测仪表盘；不要文字、logo、水印或真实人物。

## 推送前检查

推送前必须确认：

- 目标日期、输出目录、markdown 标题、frontmatter 和 `wechat-post-multi.json` 日期完全一致
- `reviewed.json` 或 `reviewed.jsonl` 中所有保留论文的 `authors_org` 不为空且非占位
- `wechat-post.md`、`wechat-post-all.md`、`wechat-post-multi.json` 存在
- `cover.png` 存在且是真实 PNG/JPG
- `scripts/wechat/.baoyu-skills/.env` 已填写微信凭据

推送命令：

```bash
cd "$REPO_ROOT/scripts/wechat"
PATH="$HOME/.bun/bin:$PATH" bun ./wechat-api.ts "$RUN_DIR/wechat-post.md" \
  --author "Thundax" \
  --cover "$RUN_DIR/cover.png" \
  --multi-manifest "$RUN_DIR/wechat-post-multi.json"
```

## 异常处理

- `40164 invalid ip`：让用户把当前出口 IP 加入公众号白名单
- `40125 invalid appsecret`：检查 `WECHAT_APP_SECRET`
- `No cover image`：先确认 `cover.png` 路径和文件格式
- 作者/机构缺失：禁止推送，先补齐
