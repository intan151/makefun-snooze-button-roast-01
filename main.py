"""Snooze Button Roast entry.

Writes a single-line roast of an alarm clock ringing at 6 AM on a
Saturday to /output/entry.txt. Deterministic: no network, no randomness,
no clock, no environment input. The text is a fixed constant.
"""

import os

ENTRY = (
    "At 6 AM on a Saturday, my alarm clock screamed like an intern who "
    "just discovered overtime pay \u2014 loud, useless, and weirdly proud "
    "of itself."
)


def self_check(text: str) -> None:
    """Gate self-check: mirrors the sealed scorer's gate.

    Must pass before anything is written. Raises AssertionError on failure.
    """
    assert isinstance(text, str)
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text.strip(), "entry must not be only white space"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert all(ord(c) >= 0x20 or c in "\t" for c in text), "no control chars"
    assert all(ord(c) != 0x7F for c in text), "no DEL char"
    text.encode("utf-8")  # must be valid UTF-8 text


def main() -> None:
    self_check(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    # Verify what was actually written.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "written output differs from ENTRY"
    self_check(written)


if __name__ == "__main__":
    main()
