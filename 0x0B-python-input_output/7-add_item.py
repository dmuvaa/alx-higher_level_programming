#!/usr/bin/python3

"""Imports multiple python modules."""


import sys
from typing import List
from os import path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def add_item(args: List[str]) -> None:
    """Function that adds all argument from a Pythhon List."""
    filename = "add_item.json"
    if path.exists(filename):
        items = load_from_json_file(filename)
    else:
        items = []
    items += args[1:]
    save_to_json_file(items, filename)

if __name__ == "__main__":
    add_item(sys.argv)
