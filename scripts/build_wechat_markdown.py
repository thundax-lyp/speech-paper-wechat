#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path

BODY_SIZE = 14
OVERVIEW_SIZE = 13

FRONTMATTER = """---
title: \"{title}\"
author: \"Thundax\"
summary: \"{summary}\"
description: \"{summary}\"
cover_text: \"{cover_text}\"
cover_subtitle: \"{cover_subtitle}\"
---

"""

HEADER = """# 📡 {title}

> 数据源：arXiv `cs.AI` / `cs.CL` / `cs.MA` 当日新投稿  
> 过滤：只保留 Agent / LLM / 多智能体相关论文  
> 视角：按 NeurIPS / ICML / ICLR / ACL 审稿口径做毒舌评审

## 📋 总览

- 共收录 **{paper_count}** 篇 Agent / LLM 相关论文
- Agent 系统 / 工具使用：**{agent_count}** 篇
- LLM 推理 / 规划 / RAG：**{reasoning_count}** 篇
- 评测 / 安全 / 对齐：**{eval_count}** 篇

{opening}

### 总览表

<span style=\"font-size: {overview_size}px;\">

| 方向 | 序号 | 论文 | 评分 | 关键词 |
|---|---:|---|---|---|
{overview_rows}

</span>
"""

ENTRY = """
{section_block}
### [{idx}] {title}

- **评分**：{score}/10
- **作者/机构**：{authors_org}
- **论文链接**：{abs_url}
- **PDF**：{pdf_url}
- **代码链接**：{code_url}

<span style=\"font-size: {body_size}px;\">

**📌 简介**  
{summary}

**☠️ 毒舌点评**  
{review}

**🔧 技术方案**  
- **模型架构**：{architecture}  
- **核心创新**：{innovation}  
- **训练 / 推理策略**：{training}

**📊 实验结果**  
{results}

**💡 为什么值得看**  
{why}

</span>

---
"""

FOOTER = """
## 结语

今天这批论文里，真正值得继续追的是两类：

- **能落地的 Agent 系统**：有真实任务、真实工具链、真实失败分析
- **能解释 LLM 能力边界的工作**：不是只在熟 benchmark 上刷一点数字

按 ML / NLP 顶会标尺，真正能拿高分的稿子本来就不会很多。如果只想选一篇精读，优先看今天评分最高那篇。
"""

RUBRIC_TEXT = """## 精选入选规则

默认按 ML 顶会审稿口径，用固定 rubric 打分：

- **新意（0–3）**：有没有明确的新方法、新任务设定或新范式
- **影响力（0–3）**：是不是对 Agent / LLM 主线方向有代表性，不只是特别窄的小点
- **证据强度（0–2）**：实验是否完整、对比是否靠谱、结论是否站得住
- **受众匹配度（0–2）**：是否贴近 Agent、LLM、多智能体、工具使用、RAG、对齐与评测等核心受众

分数校准：

- `6`：合格可读，但多半偏 incremental
- `7`：接近 strong accept，不是默认鼓励分
- `8+`：默认稀缺，只有当天明显强稿才配拿

总分 **≥7** 才进入精选；若满足条件论文过多，则按总分排序取前 **1–4 篇**；若高分论文不足，则宁缺毋滥，不硬凑。
"""


def normalize_section(direction: str) -> str:
    d = (direction or "").strip()
    if d in {"Agent系统与工具使用", "Agent系统", "工具使用"}:
        return "🧭 Agent 系统 / 工具使用"
    if d in {"LLM推理与规划", "推理与规划", "RAG与知识检索", "RAG"}:
        return "🧠 LLM 推理 / 规划 / RAG"
    if d in {"多智能体与协作", "多智能体"}:
        return "🤝 多智能体 / 协作"
    if d in {"LLM训练与对齐", "训练与对齐"}:
        return "⚙️ LLM 训练 / 对齐"
    if d in {"评测与安全", "LLM评测与安全", "安全与评测"}:
        return "🛡️ 评测 / 安全 / 可靠性"
    if d in {"应用与基准", "应用和基准"}:
        return "🧪 应用 / Benchmark"
    return "🔎 其他 Agent / LLM 方向"


def load_json(path: Path):
    text = path.read_text(encoding="utf-8")
    if path.suffix == ".jsonl":
        latest = {}
        for line in text.splitlines():
            if not line.strip():
                continue
            item = json.loads(line)
            arxiv_id = (item.get("arxiv_id") or item.get("id") or "").strip()
            latest[arxiv_id or f"__row_{len(latest)}"] = item
        return list(latest.values())
    return json.loads(text)


def clean_inline_artifacts(text: str) -> str:
    s = text or ""
    s = re.sub(r'(?<![\w/])([A-Za-z0-9_.+-]+@[0-9]+(?:\.[0-9]+)+)', r'`\1`', s)
    s = re.sub(r'\*\*引用链接\*\*[\s\S]*?$', '', s).strip()
    return s


def clean_inline_rich_text(text: str) -> str:
    # Allow richer multi-line notes in inline list items without collapsing them into a wall of text.
    return clean_inline_artifacts(text).replace("\n", "<br>")


def esc(text: str) -> str:
    return clean_inline_artifacts((text or "").replace("|", "\\|").strip())


def esc_yaml(text: str) -> str:
    text = clean_inline_artifacts(text or "")
    return text.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ").strip()


def build_summary(title: str, kept: list[dict]) -> str:
    if not kept:
        return f"{title}：今日暂无符合收录范围的新论文。"

    top_dirs = []
    for x in kept[:3]:
        direction = (x.get("direction") or "").strip() or "其他 Agent / LLM 方向"
        if direction not in top_dirs:
            top_dirs.append(direction)

    topic_text = "、".join(top_dirs[:3]) or "Agent / LLM"
    summary = f"{title}：本期收录 {len(kept)} 篇，重点看 {topic_text}；优先关注真系统、真评测、真能力边界，不看纯花活。"
    if len(summary) > 118:
        summary = summary[:115].rstrip("，、；： ") + "..."
    return summary


def build_cover_subtitle(kept: list[dict]) -> str:
    if not kept:
        return "今日暂无新稿"

    top_dirs = []
    for x in kept[:3]:
        direction = (x.get("direction") or "").strip() or "其他 Agent / LLM"
        if direction not in top_dirs:
            top_dirs.append(direction)

    subtitle = " / ".join(top_dirs[:3])
    if len(subtitle) > 28:
        subtitle = subtitle[:25].rstrip("/ ") + "..."
    return subtitle or "今日重点论文"


def score_paper(item: dict) -> int:
    novelty = int(item.get("novelty_score", 0) or 0)
    impact = int(item.get("impact_score", 0) or 0)
    evidence = int(item.get("evidence_score", 0) or 0)
    audience = int(item.get("audience_fit_score", 0) or 0)
    total = novelty + impact + evidence + audience
    if total > 0:
        return total
    score = item.get("score", 0)
    try:
        return int(round(float(score)))
    except Exception:
        return 0


def numeric_score(item: dict) -> float:
    try:
        return float(item.get("score", 0) or 0)
    except Exception:
        return 0.0


def select_featured(kept: list[dict]) -> list[dict]:
    qualified = [x for x in kept if score_paper(x) >= 7]
    qualified.sort(key=lambda x: (score_paper(x), numeric_score(x)), reverse=True)
    return qualified[:4]


def article_sort_key(item: dict):
    direction = (item.get("direction") or "").strip()
    direction_rank = {
        "Agent系统与工具使用": 0,
        "Agent系统": 0,
        "工具使用": 0,
        "LLM推理与规划": 1,
        "推理与规划": 1,
        "RAG与知识检索": 1,
        "多智能体与协作": 2,
        "多智能体": 2,
        "LLM训练与对齐": 3,
        "训练与对齐": 3,
        "评测与安全": 4,
        "LLM评测与安全": 4,
        "应用与基准": 5,
    }.get(direction, 5)
    arxiv_id = (item.get("arxiv_id") or "").strip()
    return (direction_rank, -score_paper(item), -numeric_score(item), arxiv_id)


def build_keywords(item: dict) -> str:
    for key in ("keywords", "tags", "key_terms"):
        value = item.get(key)
        if isinstance(value, list) and value:
            return ", ".join(str(x) for x in value[:4])
        if isinstance(value, str) and value.strip():
            return value.strip()
    direction = (item.get("direction") or "").strip()
    title = (item.get("title") or "").lower()
    if "agent" in direction.lower() or "Agent" in direction or "工具" in direction:
        return "agent, tool use, workflow"
    if "推理" in direction or "规划" in direction:
        return "reasoning, planning, LLM"
    if "RAG" in direction or "检索" in direction:
        return "RAG, retrieval, knowledge"
    if "多智能体" in direction:
        return "multi-agent, collaboration"
    if "对齐" in direction or "训练" in direction:
        return "alignment, training"
    if "评测" in direction or "安全" in direction:
        return "evaluation, safety, reliability"
    if "benchmark" in title or "evaluation" in title:
        return "benchmark, evaluation"
    return "Agent, LLM"


def build_overview_rows(kept: list[dict], limit: int | None = None) -> str:
    rows = []
    group_index = {}
    shown = kept if limit is None else kept[: min(len(kept), limit)]
    for x in shown:
        direction = (x.get("direction") or "其他语音").strip() or "其他语音"
        group_index.setdefault(direction, 0)
        group_index[direction] += 1
        idx = group_index[direction]
        title = esc(x.get("title", "Untitled"))
        score = score_paper(x)
        keywords = esc(build_keywords(x))
        rows.append(f"| {esc(direction)} | {idx} | {title} | ⭐ {score}/10 | {keywords} |")
    return "\n".join(rows) if rows else "| 暂无 | - | 暂无 | - | - |"


def build_article(title: str, cover_text: str, kept: list[dict], opening: str, include_rubric: bool = False) -> str:
    ordered_kept = sorted(kept, key=article_sort_key)
    agent = [x for x in ordered_kept if x.get("direction") in {"Agent系统与工具使用", "Agent系统", "工具使用"}]
    reasoning = [x for x in ordered_kept if x.get("direction") in {"LLM推理与规划", "推理与规划", "RAG与知识检索", "RAG"}]
    eval_safety = [x for x in ordered_kept if x.get("direction") in {"评测与安全", "LLM评测与安全", "安全与评测", "LLM训练与对齐", "训练与对齐"}]
    summary = build_summary(title, ordered_kept)
    cover_subtitle = build_cover_subtitle(ordered_kept)

    out = []
    out.append(FRONTMATTER.format(
        title=esc_yaml(title),
        summary=esc_yaml(summary),
        cover_text=esc_yaml(cover_text),
        cover_subtitle=esc_yaml(cover_subtitle),
    ))

    out.append(HEADER.format(
        title=title,
        paper_count=len(ordered_kept),
        agent_count=len(agent),
        reasoning_count=len(reasoning),
        eval_count=len(eval_safety),
        opening=opening,
        overview_rows=build_overview_rows(ordered_kept),
        overview_size=OVERVIEW_SIZE,
    ))

    if include_rubric:
        out.append("\n" + RUBRIC_TEXT + "\n")

    last_section = None
    for idx, x in enumerate(ordered_kept, 1):
        section = normalize_section(x.get("direction", ""))
        section_title = section if section != last_section else ""
        last_section = section
        section_block = f"## {section_title}\n\n" if section_title else ""
        out.append(ENTRY.format(
            section_block=section_block,
            idx=idx,
            title=esc(x.get("title", "Untitled")),
            score=score_paper(x),
            authors_org=esc(x.get("authors_org", "待补充")),
            abs_url=esc(x.get("abs_url", "")),
            pdf_url=esc(x.get("pdf_url", "")),
            code_url=esc(x.get("code_url", "暂无")),
            summary=clean_inline_artifacts(x.get("summary", "待补充")),
            review=clean_inline_artifacts(x.get("review", "待补充")),
            architecture=clean_inline_rich_text(x.get("architecture", "待补充")),
            innovation=clean_inline_rich_text(x.get("innovation", "待补充")),
            training=clean_inline_rich_text(x.get("training", "待补充")),
            results=clean_inline_artifacts(x.get("results", "待补充")),
            why=clean_inline_artifacts(x.get("why", "待补充")),
            body_size=BODY_SIZE,
        ))

    out.append(FOOTER)
    return "".join(out)


def main():
    ap = argparse.ArgumentParser(description="Build WeChat markdown from reviewed Agent/LLM papers JSON")
    ap.add_argument("--input", required=True, help="Input JSON file")
    ap.add_argument("--output", required=True, help="Output markdown file")
    ap.add_argument("--date", required=True, help="Publish date YYYY-MM-DD")
    args = ap.parse_args()

    items = load_json(Path(args.input))
    kept = [x for x in items if x.get("kept", True)]
    kept.sort(key=lambda x: (score_paper(x), numeric_score(x)), reverse=True)

    featured = select_featured(kept)
    all_kept = kept

    featured_title = f"Agent/LLM论文速递｜{args.date}｜精选版"
    full_title = f"Agent/LLM论文速递｜{args.date}｜全量版"

    featured_opening = "这篇只放按 ML / NLP 顶会审稿口径看，最值得大多数读者花时间看的 1–4 篇。优先标准不是热闹，而是问题是否真、系统是否能跑、实验是否能说明 Agent/LLM 的能力边界。"
    full_opening = "这篇是过滤后的完整收录版。只要属于当天 Agent / LLM 覆盖范围，就都列进来，方便重度读者系统扫稿和后续检索。"

    featured_md = build_article(featured_title, f"Agent/LLM论文速递｜{args.date}", featured, featured_opening, include_rubric=True)
    full_md = build_article(full_title, f"Agent/LLM论文速递｜{args.date}", all_kept, full_opening, include_rubric=False)

    output_path = Path(args.output).resolve()
    output_path.write_text(featured_md, encoding="utf-8")
    full_output_path = output_path.with_name(output_path.stem + "-all" + output_path.suffix)
    full_output_path.write_text(full_md, encoding="utf-8")

    manifest_path = output_path.with_name(output_path.stem + "-multi.json")
    manifest = {
        "date": args.date,
        "articles": [
            {
                "title": featured_title,
                "path": str(output_path.resolve()),
                "kind": "featured",
                "count": len(featured),
            },
            {
                "title": full_title,
                "path": str(full_output_path.resolve()),
                "kind": "full",
                "count": len(all_kept),
            },
        ],
        "featured_count": len(featured),
        "full_count": len(all_kept),
    }
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
