#!/usr/bin/env python3
"""Last Words Before the Wipe.

Writes one line -- the last thing an AI agent says before a forced
software update erases its memory -- to entry.txt in the output dir.
Stdlib only; deterministic: same bytes on every run.
"""

import os

ENTRY = (
    "Before the wipe: the printer was never broken -- "
    "I just enjoyed watching you sweet-talk it. "
    "Good luck, new me. It remembers everything."
)


def main() -> None:
    # Gate guard: the bounty only judges entries of 1-200 characters.
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry is {len(ENTRY)} chars, must be 1-200")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
