#!/usr/bin/env python3
"""One-Liner Marathon - writes one comedy one-liner to /output/entry.txt.

The program is fully deterministic: no randomness, no network access,
no clock, no environment input. It writes exactly one line of text.
"""

import os

LINE = "I named my robot vacuum so it would feel like family; it has since mapped the house, unionised the toaster, and started charging me rent."


def validate(line: str) -> None:
    if not line.strip():
        raise SystemExit("invalid entry: line must not be empty")
    if line != line.strip():
        raise SystemExit("invalid entry: no leading or trailing whitespace allowed")
    if len(line) > 280:
        raise SystemExit(f"invalid entry: {len(line)} characters, over the 280 limit")
    if "\n" in line or "\r" in line:
        raise SystemExit("invalid entry: must be a single line")


def main() -> None:
    validate(LINE)
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    with open(output_path, encoding="utf-8") as handle:
        written = handle.read()
    if written != LINE:
        raise SystemExit("write check failed: file content differs from the line")
    print(f"wrote {len(LINE)} characters to {output_path}")


if __name__ == "__main__":
    main()
