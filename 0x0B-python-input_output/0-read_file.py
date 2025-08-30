#!/usr/bin/python3
"""A module for reading and printing text files.

This module provides a function to read the content of
a text file (UTF8) and print it to stdout.
"""


def read_file(filename=""):
    """Read a text file (UTF8) and print its content to stdout.

    Args:
        filename (str): The name of the file to read (defaults to "").
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
