#!/usr/bin/python3

"""imports a JSON module."""

import json


def load_from_json_file(filename):
    """function that creates an Object from a JSON file."""
    with open("r", filename) as f:
        json.load(f, filename)
