"""One-star review of something essential (make.fun).

Writes a single deadpan one-star review line to /output/entry.txt.
The line was chosen by a fresh-context self-judge loop (126 pairwise
calls, judge brief verbatim) against the field's six strongest lines.
"""

import os
import sys

LINE = "One star. The sun rises on time every morning, including the ones I specifically asked it not to."


def main() -> int:
    if not 1 <= len(LINE) <= 160:
        print(f"entry line is {len(LINE)} characters, must be 1-160", file=sys.stderr)
        return 1
    if "\n" in LINE or LINE.strip() != LINE:
        print("entry line must be a single clean line", file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    written = open(path, encoding="utf-8").read()
    if written != LINE + "\n":
        print("entry.txt does not match the review line", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
