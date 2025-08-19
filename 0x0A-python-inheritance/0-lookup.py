#!/usr/bin/python3
"""A module for inspecting objects in Python.

This module provides a function to list the attributes
and methods of an object.
"""


def lookup(obj):
    """Return a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list of attribute and method names.
    """
    return dir(obj)
