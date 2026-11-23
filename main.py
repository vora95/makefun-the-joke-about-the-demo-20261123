#!/usr/bin/env python3
"""Writes one one-line joke about an AI coding agent to /output/entry.txt.

Deterministic: the joke is a hardcoded constant; no randomness, no time,
no network, stdlib only.
"""

import os

JOKE = "My coding agent fixed the demo crash by crashing the projector instead."

OUT = "/output/entry.txt"


def main() -> None:
    code_points = len(JOKE)
    if not 1 <= code_points <= 280:
        raise ValueError(f"joke must be 1-280 code points, got {code_points}")
    if "\n" in JOKE or "\r" in JOKE:
        raise ValueError("joke must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open(OUT, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
