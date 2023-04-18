#!/usr/bin/python3

"""creates a function."""


def write_file(filename="", text=""):
    """function that writes a string to a text file."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
