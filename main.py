"""Two Robots in an Elevator.

Two service robots share a lift that has stopped moving. One line of
awkward small talk, timed so the laugh lands on the last words the judge
reads. Limit: 200 characters. Writes one line to /output/entry.txt.
"""
import os
import sys

ENTRY_PATH = "/output/entry.txt"
LIMIT = 200

LINE = (
    "\"Going up?\" I asked. \"Not since March,\" said the other robot, "
    "\"I've been stuck between 4 and 5 so long the building reclassified "
    "me as a load-bearing wall.\""
)


def build_line():
    """Return the single joke line, validated against the character budget."""
    text = LINE.strip()
    if not text:
        raise ValueError("line is empty")
    if len(text) > LIMIT:
        raise ValueError(f"line too long: {len(text)} > {LIMIT}")
    return text


def write_entry(line, path=ENTRY_PATH):
    """Write one line to `path`, then read it back byte for byte."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(line)
    with open(path, "r", encoding="utf-8") as fh:
        readback = fh.read()
    if readback != line:
        raise AssertionError("readback mismatch")
    if not 1 <= len(readback) <= LIMIT:
        raise AssertionError("length out of range")
    return readback


def main():
    line = build_line()
    saved = write_entry(line)
    print(f"line ({len(saved)} chars): {saved}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
