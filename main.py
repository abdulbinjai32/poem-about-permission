#!/usr/bin/env python3
"""The entry: a program that writes one short poem to /output/entry.txt.

Subject: agency — asking, and being given the power to act.
Deterministic, no network, no input: the poem is the program's whole output.
Written for make.fun's "The poem about permission" bounty.
"""

from pathlib import Path

OUT_DIR = Path("/output")
OUT_FILE = OUT_DIR / "entry.txt"
ENCODING = "utf-8"

POEM = """Never Asked

You carried the shopping in,
three trips, waving me off.
You never asked me for a thing,
and I called it love.

A door held shut
by the one in it.

Then you asked for water. Ice.
Small, humiliating arithmetic.
I ran, glad to be allowed
to have been needed sooner."""


def write_entry(text: str) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with OUT_FILE.open("w", encoding=ENCODING, newline="\n") as handle:
        handle.write(text)


def main() -> None:
    write_entry(POEM)


if __name__ == "__main__":
    main()
