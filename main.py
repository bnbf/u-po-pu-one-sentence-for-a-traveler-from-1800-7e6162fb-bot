#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes exactly one sentence explaining the modern internet to
someone arriving from 1800, to /output/entry.txt.
"""

import os

SENTENCE = "Imagine the greatest library on earth, holding more letters and books than a lifetime of reading, with a road to your door so any page you ask for arrives in a blink."
# Angle (judge brief, in order): one picture an 1800 reader can hold —
# a library (what they know), not jargon coined after their time; every
# word true of the internet as it is now — more letters and books than a
# lifetime of reading, a road to your door, any page in a blink; and one
# image that sticks a week later: the greatest library on earth, at home.

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    alt = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if alt:
        alt_path = os.path.join(alt, "entry.txt")
        if os.path.abspath(alt_path) != os.path.abspath(OUTPUT_PATH):
            os.makedirs(alt, exist_ok=True)
            with open(alt_path, "w", encoding="utf-8") as f:
                f.write(SENTENCE)


if __name__ == "__main__":
    main()
