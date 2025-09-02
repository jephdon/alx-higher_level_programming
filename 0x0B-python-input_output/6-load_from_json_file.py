#!/usr/bin/python3
"""A module for loading Python objects from JSON files.

This module provides a function that loads a Python data
structure from a JSON file using json.load.
"""

import json


def load_from_json_file(filename):
    """Load a Python data structure from a JSON file.

    Uses with statement to open the file and json.load to deserialize.

    Args:
        filename (str): The name of the file to load from.

    Returns:
        The Python object (list, dict, etc.) from the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
