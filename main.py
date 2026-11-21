# The joke about the demo — hand-in program (Python 3.13, stdlib only).
#
# Writes one original one-line joke about working beside an AI coding
# agent to /output/entry.txt. The joke is a fixed string, so the program
# is deterministic: two runs write identical bytes.

import os
import sys

JOKE = (
    "My agent demoed the new dashboard for the client \u2014 the dashboard, "
    "the database password, and its honest opinion of my code."
)

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    text = JOKE
    if not 1 <= len(text) <= 280:
        raise SystemExit(f"joke is {len(text)} code points, must be 1-280")
    if not text.strip():
        raise SystemExit("joke must not be only whitespace")
    # Only ever create the output directory; never remove it — in the
    # grader it is a mounted directory and removing it fails.
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)}-character joke to {OUT_DIR}/entry.txt")


if __name__ == "__main__":
    main()
