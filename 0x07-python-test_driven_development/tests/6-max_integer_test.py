#!/usr/bin/python3
"""Testcases for the def max_integer(list=[]): function."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class that defines unittests for max_integer."""

    def test_ordered_list(self):
        """function that tests if the list of integers is ordered."""
        ordered_list = [1, 2, 3]
        self.assertEqual(max_integer(ordered_list), 3)

    def test_unordered_list(self):
        """function that tests if the list of integers is unordered."""
        unordered_list = [4, 3, 5, 2]
        self.asserEqual(max_integer(unordered_list), 4)

    def test_empty_list(self):
        """function test if the list is empty."""
        empty_list = []
        self.assertEqual(max_integer(empty_list), None)

    def test_empty_string(self):
        """function that tests whether the string has only one element."""
        one_element = [1]
        self.assertEqual(max_integer(one_element), 1)

    def test_string_list(self):
        """function that tests if the list is a string."""
        isstr = ["AlX", "Dennis", "Engineer"]
        self.assertEqual(max_integer(isstr), 'r')

    def test_mixed_list(self):
        """function that checks if the list is a mix of int and str."""
        mixed_list = ["Max", 1, "Verstappen"]
        self.assertEqual(max_integer(mixed_list))

if __name__ == '__main__':
    unittest.main()
