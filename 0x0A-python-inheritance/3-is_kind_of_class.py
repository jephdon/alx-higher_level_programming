#!/usr/bin/python3
"""A module for checking if an object is an instance of
a class or its subclass.

This module provides a function that returns True if the
object is an instance of the specified class or a subclass,
False otherwise.
"""


def is_kind_of_class(obj, a_class):
    """Check if the object is an instance of, or inherited from,
    the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or a subclass,
        False otherwise.
    """
    return isinstance(obj, a_class)
