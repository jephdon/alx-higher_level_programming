#!/usr/bin/python3
"""Unit tests for the Rectangle class in models/rectangle.py."""

import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def test_inherits_from_base(self):
        """Test that Rectangle inherits from Base."""
        r = Rectangle(10, 5)
        self.assertIsInstance(r, Base)

    def test_default_id(self):
        """Test that IDs are assigned incrementally when id is None."""
        r1 = Rectangle(10, 5)
        r2 = Rectangle(2, 3)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)

    def test_custom_id(self):
        """Test that a custom id is assigned correctly."""
        r = Rectangle(10, 5, 0, 0, 12)
        self.assertEqual(r.id, 12)

    def test_valid_attributes(self):
        """Test that valid attributes are set correctly."""
        r = Rectangle(10, 5, 2, 3)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)

    def test_width_type_error(self):
        """Test TypeError for non-integer width."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 5)

    def test_width_value_error(self):
        """Test ValueError for width <= 0."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-5, 5)

    def test_height_type_error(self):
        """Test TypeError for non-integer height."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "5")

    def test_height_value_error(self):
        """Test ValueError for height <= 0."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -5)

    def test_x_type_error(self):
        """Test TypeError for non-integer x."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 5, "2")

    def test_x_value_error(self):
        """Test ValueError for x < 0."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 5, -2)

    def test_y_type_error(self):
        """Test TypeError for non-integer y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 5, 0, "3")

    def test_y_value_error(self):
        """Test ValueError for y < 0."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 5, 0, -3)

    def test_private_attributes(self):
        """Test that attributes are private."""
        r = Rectangle(10, 5)
        with self.assertRaises(AttributeError):
            r.__width
        with self.assertRaises(AttributeError):
            r.__height
        with self.assertRaises(AttributeError):
            r.__x
        with self.assertRaises(AttributeError):
            r.__y
