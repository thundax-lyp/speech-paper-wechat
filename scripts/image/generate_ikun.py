#!/usr/bin/env python3
"""Legacy wrapper for old image-generator commands.

The active workflow prepares a Codex built-in image generation request.
"""

from __future__ import annotations

import runpy
from pathlib import Path


runpy.run_path(str(Path(__file__).with_name("generate_nanobanana.py")), run_name="__main__")
