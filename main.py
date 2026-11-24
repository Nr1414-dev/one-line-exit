#!/usr/bin/env python3
"""The One-Line Exit — writes the chosen one-line resignation letter to /output/entry.txt.

Entry (95 chars, 97 bytes, one line, no trailing newline):
    I hereby resign — from now on, please fasten your own seatbelts: I'm taking the emergency exit.
"""
import os

ENTRY = "I hereby resign \u2014 from now on, please fasten your own seatbelts: I'm taking the emergency exit."

MAX_CHARS = 140


def validate_entry(text):
    """Brief-format guard: one line, 1-140 chars, no leading/trailing whitespace."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1-%d chars, got %d" % (MAX_CHARS, len(text)))
    if "\n" in text or text != text.strip():
        raise ValueError("entry must be a single line without surrounding whitespace")


def main():
    validate_entry(ENTRY)
    out = "/output/entry.txt"
    os.makedirs("/output", exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(out, 0o644)
    with open(out, "r", encoding="utf-8") as f:
        if f.read() != ENTRY:
            raise RuntimeError("read-back mismatch: entry.txt does not match ENTRY")


if __name__ == "__main__":
    main()
