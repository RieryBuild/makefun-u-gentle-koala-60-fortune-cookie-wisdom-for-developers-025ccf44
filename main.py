"""Fortune Cookie Wisdom for Developers — entry program.

Writes one original fortune-cookie line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). The line is a fixed constant: no input, no network,
no randomness, so both grading runs produce byte-identical output.
Written with no trailing newline, as the gate counts characters.
"""

import os

FORTUNE = "The legacy code you curse was written by someone who, like you, ran out of time."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)

if __name__ == "__main__":
    main()
