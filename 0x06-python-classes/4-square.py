#!/usr/bin/python3
"""This module defines a Square class with a
private size attribute."""


class Square:
    """A class that represents a squre."""

    def __init__(self, size=0):
        """Initialize a new Square with an optional size.

        Args:
            size (int): The size of the square (defaults to 0).
        """
        self.size = size    # this calls the setter to check the size

    @property
    def size(self):
        """Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with checks.

        Args:
            value (int): The new size to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area (size times size).
        """
        return self.__size * self.__size
