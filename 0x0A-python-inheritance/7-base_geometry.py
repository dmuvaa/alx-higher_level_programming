#!/usr/bin/python3

"""creates a class."""


class BaseGeometry:
    """Base Geometry Class."""

    def area(self):
        """Class based on previous task."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Value validator."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
