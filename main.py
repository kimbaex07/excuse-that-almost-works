#!/usr/bin/env python3
"""The Excuse That Almost Works.

Writes the one line a gamer texts the boss to skip work on GTA 6 launch
week to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Pure Python standard library only.
"""

import os

LINE = (
    "My wifi died mid-update and IT says the router's firmware "
    "bricked, they're coming to my flat sometime before lunch, probably."
)


def main() -> None:
    if not (1 <= len(LINE) <= 140):
        raise ValueError(
            f"entry must be 1-140 characters, got {len(LINE)}"
        )
    if len(LINE.split()) > 20:
        raise ValueError(
            f"entry must be at most 20 words, got {len(LINE.split())}"
        )
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")
    if not LINE.strip():
        raise ValueError("entry must not be only whitespace")
    LINE.encode("utf-8")  # gate requires UTF-8 text

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
