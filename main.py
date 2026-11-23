#!/usr/bin/env python3
"""One Letter: Coffee or Tea — write exactly one letter to /output/entry.txt.

Pure standard library. The gate is strict: /output/entry.txt must be UTF-8
text of exactly 1 character, not only whitespace. So the program writes the
single byte "A" (coffee) with NO trailing newline — "A\\n" would be 2
characters and fail the gate. The file is left world-readable (0644) because
the grader collects outputs as another user.
"""

import os

LETTER = "A"  # A = coffee


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LETTER)
    # The grader collects outputs as another user: leave the file readable.
    os.chmod(path, 0o644)
    try:
        os.chmod(out_dir, 0o755)
    except OSError:
        pass


if __name__ == "__main__":
    main()
