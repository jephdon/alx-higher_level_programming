#!/usr/bin/python3
"""Unittest module for the max_integer function from 6-max_integer.py.

This module tests the max_integer function with various cases,
including empty lists, positive/negative numbers, duplicates,
and single elements.
"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test class for max_integer function."""

    def test_empty_list(self):
        """Test max_integer with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test max_integer with a list containing one element."""
        self.assertEqual(max_integer([5]), 5)

    def test_positive_numbers(self):
        """Test max_integer with a list of positive numbers."""
        self.assertEqual(max_integer([1, 3, 5, 2, 4]), 5)

    def test_negative_numbers(self):
        """Test max_integer with a list of negative numbers."""
        self.assertEqual(max_integer([-1, -5, -3, -2]), -1)

    def test_mixed_numbers(self):
        """Test max_integer with a list of mixed positive and
        negative numbers."""
        self.assertEqual(max_integer([-10, 0, 5, -5, 10]), 10)

    def test_duplicates(self):
        """Test max_integer with duplicates in the list."""
        self.assertEqual(max_integer([4, 4, 4]), 4)
        self.assertEqual(max_integer([1, 2, 3, 3, 2]), 3)

    def test_all_same_elements(self):
        """Test max_integer with all elements the same."""
        self.assertEqual(max_integer([7, 7, 7]), 7)

    def test_zero(self):
        """Test max_integer with a list containing zero."""
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([-5, 0, 5]), 5)


if __name__ == '__main__':
    unittest.main()
