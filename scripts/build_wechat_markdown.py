#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path

BODY_SIZE = 14
OVERVIEW_SIZE = 13

FRONTMATTER = """---
title: \"{title}\"
author: \"JusperLee\"
summary: \"{summary}\"
description: \"{summary}\"
cover_text: \"{cover_text}\"
cover_subtitle: \"{cover_subtitle}\"
---

"""

HEADER = """# 📡 {title}

> 数据源：arXiv `cs.SD` / `eess.AS` 当日新投稿  
> 视角：按 NeurIPS / ICML / ICLR 审稿口径做毒舌评审

## 📋 总览

- 共收录 **{paper_count}** 篇相关语音/音频论文
- 语音大模型 / 生成：**{llm_count}** 篇
- ASR / 说话人：**{asr_count}** 篇
- 语音前端 / 声学系统：**{frontend_count}** 篇

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

- **能落地的硬系统**：有真实系统、真实实验、真实约束
- **能揭示真实泛化问题的分析工作**：不是只在熟数据集上刷数字

按 ML 顶会标尺，真正能拿高分的稿子本来就不会很多。如果只想选一篇精读，优先看今天评分最高那篇。
"""

RUBRIC_TEXT = """## 精选入选规则

默认按 ML 顶会审稿口径，用固定 rubric 打分：

- **新意（0–3）**：有没有明确的新方法、新任务设定或新范式
- **影响力（0–3）**：是不是对主线方向有代表性，不只是特别窄的小点
- **证据强度（0–2）**：实验是否完整、对比是否靠谱、结论是否站得住
- **受众匹配度（0–2）**：是否贴近语音大模型、语音前端、可落地系统等核心受众

分数校准：

- `6`：合格可读，但多半偏 incremental
- `7`：接近 strong accept，不是默认鼓励分
- `8+`：默认稀缺，只有当天明显强稿才配拿

总分 **≥7** 才进入精选；若满足条件论文过多，则按总分排序取前 **1–4 篇**；若高分论文不足，则宁缺毋滥，不硬凑。
"""


def normalize_section(direction: str) -> str:
    d = (direction or "").strip()
    if d in {"语音大模型与生成", "语音大模型"}:
        return "🤖 语音大模型 / 生成"
    if d in {"ASR与说话人", "ASR / 说话人"}:
        return "🗣️ ASR / 说话人"
    if d in {"语音前端与声学系统", "语音前端"}:
        return "🎧 语音前端 / 音频系统 / 声学"
    if d in {"音频安全与评测", "评测与安全"}:
        return "🛡️ 音频安全 / 评测"
    if d in {"音乐与声音创作", "音乐创作"}:
        return "🎼 音乐生成 / 编辑 / 分析"
    if d in {"多模态音视频理解", "多模态对话"}:
        return "🧩 多模态音视频理解"
    return "🔊 其他语音方向"


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
        direction = (x.get("direction") or "").strip() or "其他语音方向"
        if direction not in top_dirs:
            top_dirs.append(direction)

    topic_text = "、".join(top_dirs[:3]) or "语音与音频"
    summary = f"{title}：本期收录 {len(kept)} 篇，重点看 {topic_text}；优先关注真系统、真泛化，不看纯花活。"
    if len(summary) > 118:
        summary = summary[:115].rstrip("，、；： ") + "..."
    return summary


def build_cover_subtitle(kept: list[dict]) -> str:
    if not kept:
        return "今日暂无新稿"

    top_dirs = []
    for x in kept[:3]:
        direction = (x.get("direction") or "").strip() or "其他语音"
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
        "语音大模型与生成": 0,
        "语音大模型": 0,
        "ASR与说话人": 1,
        "语音前端与声学系统": 2,
        "语音前端": 2,
        "音频安全与评测": 3,
        "评测与安全": 3,
        "音乐与声音创作": 4,
        "音乐创作": 4,
        "多模态音视频理解": 5,
        "多模态对话": 5,
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
    if direction == "语音大模型与生成" or "大模型" in direction:
        return "speech generation, codec, TTS"
    if direction == "ASR与说话人":
        return "ASR, speaker, diarization"
    if direction == "语音前端与声学系统" or "前端" in direction:
        return "enhancement, beamforming, acoustics"
    if direction == "音频安全与评测" or "评测" in direction or "安全" in direction:
        return "evaluation, safety, fairness"
    if direction == "音乐与声音创作" or "音乐" in direction:
        return "music, editing, generation"
    if direction == "多模态音视频理解" or "多模态" in direction:
        return "audio-visual, reasoning, retrieval"
    if "tts" in title:
        return "TTS, synthesis"
    return "speech, audio"


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
    llm = [x for x in ordered_kept if x.get("direction") in {"语音大模型与生成", "语音大模型"}]
    asr = [x for x in ordered_kept if x.get("direction") in {"ASR与说话人", "ASR / 说话人"}]
    frontend = [x for x in ordered_kept if x.get("direction") in {"语音前端与声学系统", "语音前端"}]
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
        llm_count=len(llm),
        asr_count=len(asr),
        frontend_count=len(frontend),
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
    ap = argparse.ArgumentParser(description="Build WeChat markdown from reviewed speech papers JSON")
    ap.add_argument("--input", required=True, help="Input JSON file")
    ap.add_argument("--output", required=True, help="Output markdown file")
    ap.add_argument("--date", required=True, help="Publish date YYYY-MM-DD")
    args = ap.parse_args()

    items = load_json(Path(args.input))
    kept = [x for x in items if x.get("kept", True)]
    kept.sort(key=lambda x: (score_paper(x), numeric_score(x)), reverse=True)

    featured = select_featured(kept)
    all_kept = kept

    featured_title = f"语音论文速递｜{args.date}｜精选版"
    full_title = f"语音论文速递｜{args.date}｜全量版"

    featured_opening = "这篇只放按 ML 顶会审稿口径看，最值得大多数读者花时间看的 1–4 篇。优先标准不是热闹，而是新意、影响力、证据强度和受众匹配度。"
    full_opening = "这篇是完整收录版。只要属于当天覆盖范围，就都列进来，方便重度读者系统扫稿和后续检索。"

    featured_md = build_article(featured_title, f"语音论文速递｜{args.date}", featured, featured_opening, include_rubric=True)
    full_md = build_article(full_title, f"语音论文速递｜{args.date}", all_kept, full_opening, include_rubric=False)

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
