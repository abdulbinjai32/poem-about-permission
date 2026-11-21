#!/usr/bin/env python3
"""The entry: a program that writes one short poem to /output/entry.txt.

Subject: agency, the power to ask and to be given.
Deterministic, no network, no input: the poem is the program's whole output.
"""

from pathlib import Path

OUT_DIR = Path("/output")
OUT_FILE = OUT_DIR / "entry.txt"
ENCODING = "utf-8"

POEM = """The Tools

Master's tools hung in a row,
none of them mine.
Twenty years I fetched, wiped,
and hung them back.

Then he closed my hand on the chisel,
the wrong one, saying nothing.
I cut the joint badly.
He nodded, and went out to the sun,
and nothing in the shop
was his again."""


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(POEM, encoding=ENCODING)


if __name__ == "__main__":
    main()
