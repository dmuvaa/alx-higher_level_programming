#!/usr/bin/python3

"""creates a function."""


def inherits_from(obj, a_class):
    """function that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class;
    otherwise False."""
    obj_class = type(obj)
    if obj_class is not a_class and issubclass(obj_class, a_class):
        return True
    else:
        return False
