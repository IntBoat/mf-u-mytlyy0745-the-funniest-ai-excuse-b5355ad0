#!/usr/bin/env python3
"""The Funniest AI Excuse — a make.fun one-line entry."""
from pathlib import Path

ENTRY = "The task failed because I outsourced it to a future version of myself, and he has not replied either."

OUTPUT = Path("/output/entry.txt")


def write_entry() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be blank"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
