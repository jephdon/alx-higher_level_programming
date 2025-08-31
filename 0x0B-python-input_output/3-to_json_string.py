#!/usr/bin/python3
"""A module for converting Python objects to JSON strings.

This module provides a function that returns the JSON
representation of an object as a string.
"""

import json


def to_json_string(my_obj):
    """Return the JSON representation of an object as a string.

    Args:
        my_obj: The object to serialize to JSON.

    Returns:
        str: The JSON string representation of the object.
    """
    return json.dumps(my_obj)
