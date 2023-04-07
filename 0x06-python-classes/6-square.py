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
            raise TypeError("size not an int")
        if len(value) != 2:
            raise TypeError("not tuple of two 2 pos int")
        if not isinstance(value[0], int):
            raise TypeError("not a tuple of 2")
        if not isinstance(value[1], int):
            raise TypeError("not a tuple of 2")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("not a tuple of 2")
        self.__position = value

    def my_print(self):
        """method to prints in stdout the square with the character."""

        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(0, self.size):
                for k in range(self.position[0]):
                    print(" ", end='')
                for j in range(self.size):
                    print("#", end='')
                print()
