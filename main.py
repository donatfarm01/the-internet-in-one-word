#!/usr/bin/env python3
"""Write the make.fun entry for 'The Internet in One Word'.

The entry is a single word, written to /output/entry.txt with no
trailing newline, so the file holds exactly the word and nothing else.
"""

import os

ENTRY = "unhinged"

# Self-gate, mirroring the bounty gate: one word, 1 to 30 characters,
# not only white space. A single word means no spaces inside it.
assert 1 <= len(ENTRY) <= 30, "entry must be 1 to 30 characters"
assert ENTRY.strip() == ENTRY and " " not in ENTRY, "entry must be one word"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
