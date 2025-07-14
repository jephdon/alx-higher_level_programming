#!/usr/bin/python3
"""This module defines a Square class with private size and
position attributes."""


class Square:
    """A class that represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square with an optional size
        and position."""
        self.size = size    # Uses the setter to check size
        self.position = position

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with checks."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with checks."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with '#' characters, using position."""
        if self.__size == 0:
            print()
        else:
            # Print blank lines for vertical position
            for _ in range(self.__position[1]):
                print()
            # Print the square with spaces for horizontal position
            for _ in range(self.__size):
                print(" " * self.__position[0] + '#' * self.__size)
