#!/usr/bin/python3
"""A module for appending text to a file.

This module provides a function that appends a string to a
text file (UTF8) and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """Append a string to a text file (UTF8) and return the
    number of characters added.

    If the file doesn’t exist, it is created. The function
    overwrites nothing but adds to the end.

    Args:
        filename (str): The name of the file to append to (defaults to "")
        text (str): The text to append to the file (defaults to "").

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
