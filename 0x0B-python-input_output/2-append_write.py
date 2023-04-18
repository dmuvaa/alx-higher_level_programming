#!/usr/bin/python3

"""creates a function."""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file."""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
