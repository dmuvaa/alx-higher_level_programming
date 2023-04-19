#!/usr/bin/python3

"""Creates a Python Class."""


class Student:
    """class that defines a student."""
    def __init__(self, first_name, last_name, age):
        """Function that initializes a student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """public class method to retrieve Student instance."""
        return self.__dict__
