#!/usr/bin/python3

"""creates a locked class."""

class LockedClass:
    """Class that prevents the user from dynamically creating new instance attributes."""

    __slots__ = ["first_name"]
