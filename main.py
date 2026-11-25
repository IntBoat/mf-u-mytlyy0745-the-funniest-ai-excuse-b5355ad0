#!/usr/bin/env python3
"""The Funniest AI Excuse (make.fun).

Writes the entry -- one line, the funniest excuse an AI agent gives
after failing a task -- to /output/entry.txt, where the sealed scorer
reads it. One line, no trailing newline.
"""

import os

TEXT = "I didn't fail the task \u2014 I completed it in a parallel timeline, and frankly, that version of you is much happier with the result."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
