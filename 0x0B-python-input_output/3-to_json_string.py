#!/usr/bin/python3

"""imports a JSON Module."""

import json


def to_json_string(my_obj):
    """function that returns the JSON representation of an object."""
    return json.dumps(my_obj)
