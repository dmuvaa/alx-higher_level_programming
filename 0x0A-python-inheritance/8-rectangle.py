#!/usr/bin/python3

"""Inherit from base Geometry."""


class Rectangle(BaseGeometry):
    """Base class to inherit."""

    def __init__(self, width, height):
        """Init rectangle width and height."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
