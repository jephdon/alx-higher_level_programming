#!/usr/bin/python3
"""This module defines a Square class with a private size
attribute and an area method."""


class Square:
    """A class that represents a square."""

    def __init__(self, size=0):
        """Initialize a new Square with an optional size.

        Args:
            size (int): The size of the square (defaults to 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area of the square.

        Returns:
            int: The area (size squared).
        """
        return self.__size * self.__size
