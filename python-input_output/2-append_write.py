#!/usr/bin/python3
"""Function is starting!"""


def append_write(filename="", text=""):
    """It is inside of function."""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
    return len(text)
