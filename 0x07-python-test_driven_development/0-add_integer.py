#!/usr/bin/python3
"""A module for adding two integers.

This module provides a function that adds two numbers, handling integers and
floats by casting floats to integers, and raises errors for invalid types.
"""


def add_integer(a, b=98):
    """Add two integers and return their sum.

    Floats are cast to integers before addition. Raises a TypeError if inputs
    are not integers or floats.

    Args:
        a (int or float): The first number to add.
        b (int or float, optional): The second number to add. Defaults to 98.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b are not integers or floats.

    Examples:
        >>> add_integer(1, 2)
        3
        >>> add_integer(100, -2)
        98
        >>> add_integer(2)
        100
        >>> add_integer(100.3, -2)
        98
    """
    # Check if a is an integer or float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    # Check if b is an integer or float
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    # Cast floats to integers
    a = int(a)
    b = int(b)
    # Return the sum
    return a + b
