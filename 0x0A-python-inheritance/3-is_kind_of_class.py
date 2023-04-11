#!/usr/bin/python3

"""Creates a function."""


def is_kind_of_class(obj, a_class):
    """function that returns True if the object is an instance of."""
    if isinstance(obj, a_class):
        return True
    else:
        return False
