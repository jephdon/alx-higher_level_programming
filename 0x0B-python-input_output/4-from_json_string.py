#!/usr/bin/python3
"""A module for converting JSON strings to Python objects.

This module provides a function that returns a Python data
structure from a JSON string.
"""

import json


def from_json_string(my_str):
    """Return a Python data structure represented by a JSON string.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        The Python object (list, dict, etc.) from the JSON string.
    """
    return json.loads(my_str)
