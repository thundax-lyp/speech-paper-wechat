#!/usr/bin/env python3
"""Compatibility wrapper for the old nanobanana entry point.

The default cover workflow now uses Codex built-in image generation. This file
keeps old commands from failing mysteriously and prepares the same Codex image
request as scripts/image/generate_codex_cover.py.
"""

from __future__ import annotations

import runpy
from pathlib import Path


runpy.run_path(str(Path(__file__).with_name("generate_codex_cover.py")), run_name="__main__")
