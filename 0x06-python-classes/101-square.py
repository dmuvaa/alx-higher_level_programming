#!/usr/bin/python3

"""class Square that defines a square based on previous square."""


class Square:
    """Private instance attribute called size."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Args:
            size of square
        """
        self.size = size
        self.position = position

    def area(self):
        """
        finds area of square
        Returns:
            the area of the square
        """

        return self.__size ** 2

    @property
    def size(self):
        """method to return the size value."""

        return self.__size

    @size.setter
    def size(self, value):
        """method that sets the value size."""

        if not isinstance(value, int):
            raise TypeError("size is not int")
        elif value < 0:
            raise ValueError("Value can't be less than zero")
        else:
            self.__size = value

    @property
    def position(self):
        """method to get/set square position."""

        return self.__position

    @position.setter
    def position(self, value):
        """Method to returns the size value."""

        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """method to prints in stdout the square with the character."""

        print(self.__str())

    def __str__(self):
        """define square representation."""
        if self.size == 0:
            return ""
        else:
            rows = []
            for i in range(self.position[1]):
                rows.append("")
            for i in range(0, self.size):
                row = " " * self.position[0] + "#" * self.size
                rows.append(row)
            return "\n".join(rows)
