#!/usr/bin/python3

"""creates a locked class."""


class LockedClass:
    """Class to prevent user from creating new instance attributes."""

    __slots__ = ["first_name"]
