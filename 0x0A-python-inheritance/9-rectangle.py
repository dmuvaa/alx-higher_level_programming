#!/usr/bin/python3

"""Rectangle to inherit from Base Geometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle Class."""
    def __init__(self, width, height):
        """Init rectangle width and height."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area."""
        return self.__width * self.__height

    def __str__(self):
        """Returns a printable string."""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
