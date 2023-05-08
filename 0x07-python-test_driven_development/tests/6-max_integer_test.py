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

    def test_max_beginning(self):
        """test if string has max at the beginning."""
        max_element = [5, 4, 3, 2, 1]
        self.assertEqual(max_integer(max_element), 5)

    def test_max_end(self):
        """test is the max is at the end."""
        max_end = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(max_end), 5 )

    def test_max_middle(self):
        """funtion that tests is max is at midddle."""
        max_middle = [1, 2, 5, 3, 4]
        self.assertEqual(max_integer(max_element), 5)

    def test_number_negative(self):
        """function that tests if the list has a negative number."""
        is_neg = [1, -1, 5, 6]
        self.assertEqual(max_integer(is_neg), -1)

    def test_neg_only(self):
        """function that checks if the list has negative numbers only."""
        neg_only = [-5, -4, -3, -2, -1]
        self.assertEqual(max_integer(neg_only))

if __name__ == '__main__':
    unittest.main()
