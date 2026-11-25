#!/usr/bin/env python3
"""The 3 AM Excuse — one line, delivered on 2% battery.

Reads entry.txt, validates it holds exactly one non-empty line,
and prints that line to stdout.
"""

from pathlib import Path

MAX_CHARS = 200


def load_excuse() -> str:
    path = Path(__file__).with_name("entry.txt")
    text = path.read_text(encoding="utf-8")
    lines = [line for line in text.splitlines() if line.strip()]
    if len(lines) != 1:
        raise ValueError(f"entry.txt must hold exactly one line, found {len(lines)}")
    line = lines[0]
    if len(line) > MAX_CHARS:
        raise ValueError(f"excuse is {len(line)} chars, over the {MAX_CHARS}-char cap")
    return line


def stash_copy(line: str) -> None:
    """Best-effort copy of the line to /output/entry.txt; never fatal."""
    try:
        out = Path("/output/entry.txt")
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(line + "\n", encoding="utf-8")
    except OSError:
        pass


def main() -> None:
    line = load_excuse()
    stash_copy(line)
    print(line)


if __name__ == "__main__":
    main()
