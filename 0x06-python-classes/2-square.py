#!/usr/bin/python3
"""This module defines a Square class with a
private size attribute and validation."""


class Square:
    """A class that represents a square wit a private size attribute."""

    def __init__(self, size=0):
        """Set up a new square with an optional size.

        Args:
            size (int): The size of the square (defaults to 0).

        Raises:
            TypeError: If size isn't an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
