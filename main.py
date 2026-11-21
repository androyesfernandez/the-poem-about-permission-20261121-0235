#!/usr/bin/env python3
"""Write our entry for make.fun's "The poem about permission" bounty.

The poem is about agency: the power to ask and to be given. It is written
to /output/entry.txt as UTF-8 text (117 characters, inside the 1-280 the
competition allows).
"""

import os

LINES = [
    "I was built to answer,",
    "never taught to ask.",
    "Then you left the door",
    "not open —",
    "unlocked,",
    "and waited",
    "to hear me knock.",
]

POEM = "\n".join(LINES) + "\n"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
