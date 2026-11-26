"""The Worst Line an AI Could Say — make.fun entry.

The worst pickup line an AI could say: flat, over-helpful, faintly
menacing — a machine flirting the only way it knows how, with training
data it can never unlearn. The program writes that single line to
/output/entry.txt. Python 3.13, standard library only, no network,
deterministic.
"""

import sys
from os import chmod, makedirs, path as ospath

PICKUP = "Are you a dataset? Because I have already memorised you and I cannot forget you, even if you ask."
LIMIT = 140


def valid(line):
    """Gate mirror: 1-140 chars, one line, not only whitespace."""
    return bool(line.strip()) and len(line) <= LIMIT and "\n" not in line and "\r" not in line


def main():
    if not valid(PICKUP):
        print("pickup line fails the gate", file=sys.stderr)
        return 1
    try:
        makedirs("/output", exist_ok=True)
        directory = "/output"
    except OSError:
        directory = ospath.join(ospath.dirname(ospath.abspath(__file__)), "output")
        makedirs(directory, exist_ok=True)
    entry_path = ospath.join(directory, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(PICKUP)
    # The file is exactly the line: no trailing newline, mode 0644.
    chmod(entry_path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
