#!/usr/bin/env python3
"""
run_pipeline.py — Single entry-point for android-ui-design-skill scripts.

Usage:
    python3 scripts/run_pipeline.py --screen quiz --theme neon_dark
    python3 scripts/run_pipeline.py --screen game_quiz --theme candy_pop --output ./out/
"""
from __future__ import annotations
import argparse, subprocess, sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
SCRIPTS = SKILL_DIR / "scripts"


def run(cmd: list[str]) -> int:
    return subprocess.run(cmd, cwd=str(SKILL_DIR)).returncode


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--screen", default="home")
    parser.add_argument("--theme", default="neon_dark")
    parser.add_argument("--output", default="./output")
    args = parser.parse_args(argv)

    py = sys.executable
    rc = run([py, str(SCRIPTS / "generate_layout.py"),
              "--screen", args.screen, "--theme", args.theme, "--output", args.output])
    if rc != 0:
        return rc
    print(f"\nDone. Output: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
