#!/usr/bin/python3
"""A module for writing text to a file.

This module provides a function that writes a string to a
text file (UTF8) and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """Write a string to a text file (UTF8) and return the number
    of characters written.

    The function creates the file if it doesn't exist and
    overwrites it if it does.

    Args:
        filename (str): The name of the file to write to (defaults to "").
        text (str): The text to write to the file (defaults to "").

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
