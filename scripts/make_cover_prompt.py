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
        f"{item.get('title', 'Untitled')}（{item.get('direction', '其他相关音频')}）"
        for item in top
    )
    prompt = f"""为微信公众号文章《语音论文速递》生成一张内容感知封面图。
要求：像素风格微信公众号封面图，宽幅横版构图，适合文章头图，复古 8-bit / 16-bit 像素艺术风格。
画面简洁但有细节，主体突出，围绕当天重点论文主题进行场景化设计，具有故事感和视觉焦点。
背景有层次，色彩鲜明但不过于杂乱，不要预留标题区，不要留白，画面尽量铺满，但仍然保持主体清晰。
整体干净、吸睛、适合社交媒体传播，现代像素插画质感。
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
