#!/usr/bin/python3
"""A module for saving Python objects to JSON files.

This module provides a function that writes an object to a
text file using its JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using its JSON representation.

    Uses with statement to handle the file.

    Args:
        my_obj: The object to serialize to JSON and save.
        filename (str): The name of the file to write to.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
