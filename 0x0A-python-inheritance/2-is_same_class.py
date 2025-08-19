#!/usr/bin/python3
"""A module for checking if an object is exactly an instance
of a specified class.

This module provides a function that returns True if the
object is an instance of the class, but not a subclass.
"""


def is_same_class(obj, a_class):
    """Check if the object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is exactly an instance of a_class,
        False otherwise.
    """
    return type(obj) == a_class
