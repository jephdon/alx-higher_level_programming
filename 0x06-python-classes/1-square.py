#!/usr/bin/python3
"""This module defines a class Square with a private size attribute."""


class Square:
    """A class that defines a square with a private size attribute.

    Attributes:
        __size (int): The size of the square (private).
    """

    def __init__(self, size):
        """Initialize a new Square with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
