#!/usr/bin/python3

"""Creates a class named rectangle."""


class Rectangle:
    """creates a class in called rectangle."""

    def __init__(self, width=0, height=0):
        """Method to initialize width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Method to set width."""
        return self.__width

    @width.setter
    def width(self, value):
        """method to define width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Method to set height."""
        return self.__height

    @height.setter
    def height(self, value):
        """method to define height of rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Gets the area or the rectangle."""
        if width or height == 0:
            area == 0

        return self.__width * self.__height

    def perimeter(self):
        """Gets perimeter of the rectangle."""
        if width or height == 0:
            perimeter == 0

        return (self.__width + self.__height) * 2
