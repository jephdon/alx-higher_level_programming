#!/usr/bin/python3
"""A module defining a base class for geometry with validation.

This module provides BaseGeometry with an area method
(not implemented) and integer validation.
"""


class BaseGeometry:
    """A base class for geometry with area and validation methods."""

    def area(self):
        """Raise an exception indicating that area is not implemented.

        Raises:
            Exception: Always, with "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer.

        Args:
            name (str): The name of the attribute (for error messages).
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
