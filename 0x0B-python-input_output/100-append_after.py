#!/usr/bin/python3

"""creates a function."""


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of text to a file."""
    text = ""
    with open(filename) as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
