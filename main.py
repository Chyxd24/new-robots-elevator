"""Two Robots in an Elevator.

One line of awkward small talk one robot says to another mid-ride.
The laugh lands on the last words. Limit: 200 characters.
Writes exactly one line to /output/entry.txt.
"""
import os

LINE = (
    "\"Going up?\" I asked. \"Can't tell anymore,\" said the other robot, "
    "\"I've been stuck between floors 4 and 5 since March — kind of "
    "like this building's IT budget.\""
)

LIMIT = 200


def build_line() -> str:
    text = LINE.strip()
    if len(text) > LIMIT:
        raise ValueError(f"line too long: {len(text)} chars (limit {LIMIT})")
    if len(text) < 1:
        raise ValueError("line is empty")
    return text


def main() -> int:
    line = build_line()
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(line)
    # readback assert — the file must round-trip byte for byte
    with open(path, "r", encoding="utf-8") as fh:
        readback = fh.read()
    assert readback == line, "readback mismatch"
    assert 1 <= len(readback) <= LIMIT, "length out of range"
    print(f"line ({len(readback)} chars): {readback}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
