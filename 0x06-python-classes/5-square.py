#!/usr/bin/python3
"""class Square that defines a square based on previous square."""


class Square:
    """Private instance attribute called size."""

    def __init__(self, size=0):
        """
        Args:
            size of square
        """

        if not isinstance(size, int):
            raise TypeError("size is not integer")
        elif size < 0:
            raise ValueError("size can't be less than zero")
        else:
            self.__size = size

    def area(self):
        """
        finds area of square
        Returns:
            the area of the square
        """

        return self.__size ** 2

    @property
    def size(self):
        """Method to returns the size value."""

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

    def my_print(self):
        """method to prints in stdout the square with the character."""

        if not self.__size:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()
