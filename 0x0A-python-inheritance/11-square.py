#!/usr/bin/python3

"""Square#2."""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """class that inherits square frim rectangle."""
    def __init__(self, size):
        """Initialize the Square."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
