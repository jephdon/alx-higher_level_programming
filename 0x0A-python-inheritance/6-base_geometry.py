#!/usr/bin/python3
"""This module defines a BaseGeometry class with an area method
that raises an exception."""


class BaseGeometry:
    """A base class for geometry with an unimplemented area method."""

    def area(self):
        """Raise an exception indicating that area is not implemented.

        Raises:
            Exception: Always, with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")
