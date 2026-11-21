#!/usr/bin/env python3
"""The entry: a program that writes one short poem to /output/entry.txt.

Subject: agency, the power to ask and to be given.
Deterministic, no network, no input: the poem is the program's whole output.
"""

from pathlib import Path

OUT_DIR = Path("/output")
OUT_FILE = OUT_DIR / "entry.txt"
ENCODING = "utf-8"

POEM = """The Reference

You wrote my name for a job I couldn't do,
and when they phoned, you said: he can.
No one had lent me certainty before.

I did it badly for a year
and kept your sentence in a drawer,
flat, folded, unspent,
the way a poor man keeps a note
he will not break."""


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with OUT_FILE.open("w", encoding=ENCODING, newline="\n") as handle:
        handle.write(POEM)


if __name__ == "__main__":
    main()
