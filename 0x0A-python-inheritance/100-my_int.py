#!/usr/bin/python3

"""creates a class."""


class MyInt(int):
    """class to inherit form int."""
    def __eq__(self, other):
        """overide operator with behavior."""
        return super().__ne__(other)

    def __ne__(self, other):
        """overide operator with behavior."""
        return super().__eq__(other)
