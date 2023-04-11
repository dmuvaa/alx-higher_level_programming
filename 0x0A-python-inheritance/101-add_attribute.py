#!/usr/bin/python3

"""Writes a function."""


def add_attribute(obj, attr_name, attr_value):
    """function that adds a new attribute to an object."""
    if not hasattr(obj, "__setattr__") or
    not callable(getattr(obj, "__setattr__")):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
