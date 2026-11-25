#!/usr/bin/env python3
"""One Line, Big Laugh — a single hilarious line, 200 characters or fewer.

The entry is one line that stands entirely on its own: no title, no setup,
no explanation around it. The program writes exactly that line to entry.txt
in the output directory.

Deterministic, no network, no input.
"""

import os
from pathlib import Path

# The entry, written by the agent in this session: 91 characters.
LINE = "I told my family I want my ashes scattered at the gym, so I finally go somewhere regularly."

MAX_CHARS = 200


def output_dir() -> Path:
    """Resolve the output directory.

    MAKEFUN_OUTPUT_DIR when set, else /output when it exists,
    else a local output/ folder next to this file.
    """
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return Path(env_dir)
    if Path("/output").is_dir():
        return Path("/output")
    return Path(__file__).resolve().parent / "output"


def main() -> None:
    line = LINE.strip()
    assert "\n" not in line, "the entry must be a single line"
    assert len(line) <= MAX_CHARS, (
        f"entry is {len(line)} characters, over the {MAX_CHARS} limit"
    )
    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    target = out / "entry.txt"
    target.write_text(line + "\n", encoding="utf-8")
    # Round-trip check: what the grader will read must be exactly the line.
    written = target.read_text(encoding="utf-8").rstrip("\n")
    assert written == line, "entry.txt content does not match the entry line"
    assert len(written) <= MAX_CHARS, "written entry exceeds the limit"
    print(f"Wrote {len(written)} characters to {target} (verified)")
    print(line)


if __name__ == "__main__":
    main()
