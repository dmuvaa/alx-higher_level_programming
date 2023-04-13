#!/usr/bin/python3

"""Defines a Square from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class to inherit Square from Rect."""

    def __init__(self, size):
        """Init a Square."""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
