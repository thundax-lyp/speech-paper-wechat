#!/usr/bin/env python3
"""Prepare a Codex built-in image generation request for a WeChat cover.

Codex's built-in image generation is an agent tool, not a normal shell API.
This helper keeps the command-line workflow reproducible by writing a compact
request file that an agent can execute with its image generation capability.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def read_prompt(args: argparse.Namespace) -> str:
    if args.prompt:
        return args.prompt.strip()
    if args.prompt_file:
        return Path(args.prompt_file).read_text(encoding="utf-8").strip()
    if not sys.stdin.isatty():
        return sys.stdin.read().strip()
    return ""


def build_request(prompt: str, output: Path, aspect_ratio: str) -> str:
    return f"""# Codex Image Generation Request

Use Codex's built-in image generation capability, not an external image API.

- Output path: `{output}`
- Aspect ratio: `{aspect_ratio}`
- Asset type: WeChat Official Account cover image
- Requirements: no text, no logo, no watermark, suitable as a wide article cover

## Prompt

{prompt}
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Prepare a request file for Codex built-in image generation. "
            "This does not call an external image API."
        )
    )
    parser.add_argument("-p", "--prompt", help="Cover image prompt text")
    parser.add_argument("--prompt-file", help="Read cover image prompt from a file")
    parser.add_argument(
        "-o",
        "--output",
        default="cover.png",
        help="Expected final cover image path",
    )
    parser.add_argument(
        "-ar",
        "--aspect-ratio",
        default="21:9",
        help="Target aspect ratio for the generated cover",
    )
    parser.add_argument(
        "-s",
        "--size",
        default="2K",
        help="Compatibility option. Codex built-in image generation chooses the concrete size.",
    )
    parser.add_argument(
        "--request-output",
        help="Where to write the Codex image request markdown",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    prompt = read_prompt(args)
    if not prompt:
        print(
            "error: prompt is required via --prompt, --prompt-file, or stdin",
            file=sys.stderr,
        )
        return 2

    output = Path(args.output)
    request_output = (
        Path(args.request_output)
        if args.request_output
        else output.with_name(output.stem + ".codex-image-request.md")
    )
    request_output.parent.mkdir(parents=True, exist_ok=True)
    request_output.write_text(
        build_request(prompt, output, args.aspect_ratio),
        encoding="utf-8",
    )

    print(f"[codex-cover] Wrote image request: {request_output}")
    print("[codex-cover] Next step for a Codex agent:")
    print(f"  1. Generate an image with the prompt in {request_output}")
    print(f"  2. Save or move the selected image to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
