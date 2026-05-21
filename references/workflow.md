# agent-llm-paper-wechat workflow

## 仓库约定

- 仓库根目录：`speech-paper-wechat/`
- 所有示例命令都从仓库根目录执行
- 运行产物默认写到：`$REPO_ROOT/runs/papers_YYYYMMDD/`
- 真实凭据只允许出现在未跟踪文件：
  - `scripts/wechat/.baoyu-skills/.env`

## 目录结构

```text
speech-paper-wechat/
  SKILL.md
  README.md
  references/
    workflow.md
  scripts/
    collect_arxiv_recent.py
    make_cover_prompt.py
    build_wechat_markdown.py
    image/
      generate_codex_cover.py
      generate_nanobanana.py
    wechat/
      package.json
      wechat-api.ts
      wechat-extend-config.ts
      wechat-image-processor.ts
      md-to-wechat.ts
      vendor/
        baoyu-md/
        baoyu-chrome-cdp/
      .baoyu-skills/
        .env.example
```

## 每日执行

1. 抓取当天 arXiv `cs.AI` / `cs.CL` / `cs.MA` 日期块
2. 在下载 PDF 前按 Agent / LLM 关键词过滤
3. 只下载保留论文的 PDF，抽首页和全文
4. 逐篇写 `reviewed.jsonl`
5. 生成精选版 + 全量版 markdown
6. 生成内容感知封面
7. 推送双文章草稿

### 1) 抓取与下载

```bash
REPO_ROOT="/path/to/speech-paper-wechat"

python3 "$REPO_ROOT/scripts/collect_arxiv_recent.py" \
  --date-heading "Wed, 20 May 2026" \
  --output runs/papers_20260520 \
  --categories cs.AI cs.CL cs.MA \
  --filter-profile agent-llm \
  --download-pdf \
  --extract-text
```

抓取脚本会写出 `metadata_unfiltered.json`、`metadata_today.json` 和
`filter_report.json`。其中 `metadata_today.json` 是过滤后、会进入 PDF 下载的论文。

### 2) 逐篇写 JSONL

每篇至少包含：

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

推荐 `direction` 固定在：

- `Agent系统与工具使用`
- `LLM推理与规划`
- `RAG与知识检索`
- `多智能体与协作`
- `LLM训练与对齐`
- `评测与安全`
- `应用与基准`

### 3) 生成 markdown

```bash
python3 "$REPO_ROOT/scripts/build_wechat_markdown.py" \
  --input runs/papers_20260520/reviewed.jsonl \
  --output runs/papers_20260520/wechat-post.md \
  --date 2026-05-20
```

### 4) 生成封面

```bash
python3 "$REPO_ROOT/scripts/make_cover_prompt.py" \
  --input runs/papers_20260520/reviewed.jsonl \
  --output runs/papers_20260520/cover_prompt.txt

python3 "$REPO_ROOT/scripts/image/generate_codex_cover.py" \
  --prompt-file runs/papers_20260520/cover_prompt.txt \
  -ar 21:9 \
  -s 2K \
  -o runs/papers_20260520/cover.png
```

该命令会写出 `runs/papers_20260520/cover.codex-image-request.md`。在 Codex
环境中，agent 应读取该请求，使用内置图片生成能力创建封面，并将最终图片保存为
`runs/papers_20260520/cover.png`。

### 5) 推送草稿

```bash
cd "$REPO_ROOT/scripts/wechat"
npx -y bun ./wechat-api.ts "$REPO_ROOT/runs/papers_20260520/wechat-post.md" \
  --author "Thundax" \
  --cover "$REPO_ROOT/runs/papers_20260520/cover.png" \
  --multi-manifest "$REPO_ROOT/runs/papers_20260520/wechat-post-multi.json"
```

## 敏感信息

- `scripts/wechat/.baoyu-skills/.env` 不进 git
- 只提交 `.env.example`

## 常见错误

- `40164 invalid ip`：公众号后台 IP 白名单不包含当前出口
- `40125 invalid appsecret`：`WECHAT_APP_SECRET` 不匹配当前公众号
- `Cannot find package 'baoyu-md'`：先确认 `scripts/wechat/vendor/` 存在，再跑 `bun install`
- `No cover image`：先确认 Codex 封面图已保存到 `--cover` 指定路径
- `Format mismatch`：封面文件名和真实格式不一致，通常可接受
