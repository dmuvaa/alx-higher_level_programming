#!/usr/bin/python3

"""creates a function."""


def class_to_json(obj):
    """function that returns the dictionary description."""
    return obj.__dict__
