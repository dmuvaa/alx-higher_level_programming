#!/usr/bin/python3

"""Creates a class named rectangle."""


class Rectangle:
    """creates a class in called rectangle."""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    width.setter

    def width(self, value):
        if not isinstance(int, width):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return self.__height

    height.setter

    def height(self, value):
        if not isinstance(int, height):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")

        return self.__height
