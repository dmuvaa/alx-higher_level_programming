#!/usr/bin/python3

"""Creates a Python Class."""


class Student:
    """class that defines a student."""
    def __init__(self, first_name, last_name, age):
        """Function that initializes a student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """public method that returns student dict to JSON."""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
