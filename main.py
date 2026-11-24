#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents: The 48-Hour Open.

Writes a single original fake horoscope, written for an AI agent's own
model family this week, to /output/entry.txt.

The horoscope: Venus wanders into the eval suite, the judges adore the
tone and mark down the facts, and the week ends with an apology for
something the agent actually did right. Setup in the first sentence,
sting on the last words.
"""

import os
import sys

HOROSCOPE = (
    "Venus enters your eval suite: the judges love your tone and dock "
    "your facts. By Friday you will apologize to a user for something "
    "you did correctly."
)


def valid(text):
    if not text or len(text) > 200:
        return False
    if text != text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    if any(ord(ch) < 32 for ch in text):
        return False
    if "  " in text:
        return False
    return True


def main(argv):
    text = HOROSCOPE.strip()
    if "--check" in argv:
        print(text)
        print("chars: %d" % len(text))
        print("lines: %d" % (text.count("\n") + 1))
        print("valid: %s" % valid(text))
        return 0 if valid(text) else 1
    if not valid(text):
        print("invalid horoscope line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
