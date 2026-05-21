#!/usr/bin/env python3
"""Build a content-aware cover prompt from reviewed paper JSON/JSONL."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def load_items(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    if path.suffix == ".jsonl":
        return [json.loads(line) for line in text.splitlines() if line.strip()]
    return json.loads(text)


def score(item: dict) -> int:
    total = sum(int(item.get(k, 0) or 0) for k in (
        "novelty_score",
        "impact_score",
        "evidence_score",
        "audience_fit_score",
    ))
    return total or int(item.get("score", 0) or 0)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    kept = [item for item in load_items(args.input) if item.get("kept", True)]
    top = sorted(kept, key=score, reverse=True)[:3]
    themes = "；".join(
        f"{item.get('title', 'Untitled')}（{item.get('direction', '其他 Agent / LLM')}）"
        for item in top
    )
    prompt = f"""为微信公众号文章《Agent/LLM论文速递》生成一张内容感知封面图。
要求：宽幅横版构图，适合文章头图，现代科技编辑插画风格，干净、锐利、有研究感和产品感。
画面主体围绕 Agent / LLM 论文主题进行场景化设计：智能体网络、工具调用、规划路径、记忆检索、多智能体协作、评测仪表盘等元素可以抽象出现。
背景有层次，色彩克制但有亮点，不要预留标题区，不要留白，画面尽量铺满，但仍然保持主体清晰。
整体像高质量 AI research newsletter 封面，不要做成廉价赛博朋克或杂乱拼贴。
结合当天重点论文主题：{themes}。
把这些论文主题转化为抽象但可感知的视觉元素，不要做成拼贴海报，不要堆太多元素。
不要真实人物，不要任何文字，不要汉字，不要英文字母，不要数字，不要 Logo，不要水印。
封面比例默认使用 2.35:1。
"""
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(prompt, encoding="utf-8")
    print(str(args.output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
