#!/usr/bin/env python3
"""One Line, Big Laugh -- a single hilarious line, 200 characters or fewer.

The entry is one line that stands entirely on its own: no title, setup,
or explanation around it. This program prints that line and writes it to
entry.txt inside $MAKEFUN_OUTPUT_DIR (or /output when the variable is
unset). Deterministic, no network, no input.
"""

import os

LINE = "My GPS sighed when I asked for the fastest route home: 'Therapy -- and I'm not elaborating.'"


def main() -> None:
    if len(LINE) > 200:
        raise SystemExit("line exceeds 200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
