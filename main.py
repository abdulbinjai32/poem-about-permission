#!/usr/bin/env python3
"""The entry: a program that writes one short poem to /output/entry.txt.

Subject: agency, the power to ask and to be given.
Deterministic, no network, no input: the poem is the program's whole output.
"""

from pathlib import Path

POEM = """Power of Attorney

She practiced her name on a receipt,
pencil, then ink,
then signed the page
that sells her house.
She looked up like a girl
done with a hard test

Each morning she asks
if she may have her pills.
I say yes. I say it
as though the yes were still
hers to give."""


def main() -> None:
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
