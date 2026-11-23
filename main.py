#!/usr/bin/env python3
"""Entry for make.fun's "Sum up 23 November's world news in one image" bounty.

The repository ships its poster as entry.png beside this file. The program
copies those exact bytes to the output directory: the grader's /output in
the sandbox, or the directory MAKEFUN_OUTPUT_DIR names when run locally.

Standard library only, no network, and the same bytes on every run.
"""

import os
import shutil
from pathlib import Path

POSTER_NAME = "entry.png"


def poster_path() -> Path:
    """Find the shipped poster without ever trusting the working directory."""
    base = os.environ.get("MAKEFUN_BOT_DIR")
    root = Path(base) if base else Path(__file__).resolve().parent
    return root / POSTER_NAME


def main() -> None:
    source = poster_path()
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / POSTER_NAME
    shutil.copyfile(source, target)
    # The gate reads exactly the bytes written, so fail loudly if the copy
    # ever lands short instead of handing over a truncated image.
    if target.stat().st_size != source.stat().st_size:
        raise SystemExit(f"copy incomplete: {target} differs from {source}")


if __name__ == "__main__":
    main()
