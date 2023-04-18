#!/usr/bin/python3

"""imports a JSON module."""

import json


def load_from_json_file(filename):
    """function that creates an Object from a JSON file."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
