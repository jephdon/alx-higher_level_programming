#!/usr/bin/python3
"""Unit tests for the Base class in models/base.py."""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def test_default_id(self):
        """Test that IDs are assigned incrementally when id is None."""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_custom_id(self):
        """Test that a custom id is assigned correctly."""
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

    def test_mixed_id(self):
        """Test that IDs continue incrementing after a custom id."""
        b5 = Base()
        self.assertEqual(b5.id, 4)

    def test_nb_objects_private(self):
        """Test that __nb_objects is not directly accessible."""
        b = Base()
        with self.assertRaises(AttributeError):
            b.__nb_objects

    def test_id_type(self):
        """Test that id can be any integer (no type checking required)."""
        b = Base(0)
        self.assertEqual(b.id, 0)
        b = Base(-5)
        self.assertEqual(b.id, -5)
