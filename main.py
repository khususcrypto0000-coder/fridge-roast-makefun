"""Fridge Roast: One Line, Biggest Laugh — make.fun one-liner entry.

Writes the single roast line to /output/entry.txt and verifies the file
is byte-identical to the in-memory entry.
"""

import os
import sys

ENTRY = (
    "My smart fridge auto-ordered eggs because it couldn't see past the jam, "
    "so now I own forty-eight eggs and an appliance that calls it "
    "'proactive inventory management.'"
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    # Gate: 1-200 characters, a single line, not only whitespace.
    if not 1 <= len(ENTRY) <= 200:
        print(f"entry length {len(ENTRY)} out of range 1-200", file=sys.stderr)
        return 1
    if ENTRY.strip() == "" or "\n" in ENTRY or "\r" in ENTRY:
        print("entry must be a single non-blank line", file=sys.stderr)
        return 1

    data = ENTRY.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)

    # Read back and verify byte-identical, and valid UTF-8.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != data:
        print("verification failed: /output/entry.txt differs from ENTRY",
              file=sys.stderr)
        return 1
    if written.decode("utf-8") != ENTRY:
        print("verification failed: /output/entry.txt is not valid UTF-8 ENTRY",
              file=sys.stderr)
        return 1

    print(f"wrote {OUTPUT_PATH} ({len(ENTRY)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
