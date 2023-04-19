#!/usr/bin/python3

"""This module imports multiple Python modules."""


import sys
from json import dump, load

if __name__ == "__main__":
    """allows a module to be run as a script."""
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    try:
        """load the contents of the file add_item.json into a list."""
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")
