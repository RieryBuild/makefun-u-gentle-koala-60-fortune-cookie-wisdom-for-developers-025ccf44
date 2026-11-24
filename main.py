"""Fortune Cookie Wisdom for Developers — entry program.

Writes one original fortune-cookie line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). The line is a fixed constant: no input, no network,
no randomness, so both grading runs produce byte-identical output.
Written with no trailing newline, as the gate counts characters.
The line turns a throwaway debug log line into the thing that outlasts
the bug, the fix, and the developer who added it.
"""

import os

FORTUNE = "The log line you added for one afternoon will outlive the bug, the fix, and you."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)

if __name__ == "__main__":
    main()
