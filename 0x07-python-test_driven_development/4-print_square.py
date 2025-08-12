#!/usr/bin/python3
"""A module for printing a square of a given size using '#'.

This module provides a function that prints a square with
validation for the size input, ensuring it's a non-negative integer.
"""


def print_square(size):
    """Print a square of '#' characters based on the given size.

    Validates that size is a non-negative integer and prints the
    square accordingly.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer or if size is a float
        and is less than 0.
        ValueError: If size is less than 0.

    Examples:
        >>> print_square(4)
        ####
        ####
        ####
        ####
        >>> print_square(1)
        #
        >>> print_square(0)

        >>> print_square(-1)
        Traceback (most recent call last):
        ValueError: size must be >= 0
        >>> print_square(3.5)
        Traceback (most recent call last):
        TypeError: size must be an integer
        >>> print_square("4")
        Traceback (most recent call last):
        TypeError: size must be an integer
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for _ in range(size):
        print("#" * size)
