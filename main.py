#!/usr/bin/env python3
"""One Line, One Laugh — make.fun bounty entry.

Writes exactly one funny line to /output/entry.txt: a single joke that
lands on a cold read, with no setup notes and no explanation.
"""

import os
import sys

JOKE = (
    "My mirror finally told me the truth: 'Objects may appear funnier "
    "than they are.' Even my reflection needs a disclaimer."
)

MAX_CHARS = 140


def main() -> int:
    line = JOKE
    # Gate self-check (mirrors the sealed scorer): UTF-8 text of 1 to 140
    # characters, not only white space, exactly one line.
    text = line.encode("utf-8").decode("utf-8")
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"gate fail: {len(text)} chars, need 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if not text.strip():
        print("gate fail: blank entry", file=sys.stderr)
        return 1
    if "\n" in text.strip():
        print("gate fail: more than one line", file=sys.stderr)
        return 1
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(text)
    print(f"chars: {len(text)} (max {MAX_CHARS})", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
