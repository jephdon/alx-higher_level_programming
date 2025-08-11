#!/usr/bin/python3
"""A module for printing a name with validation.

This module provides a function that prints a full name from first and
last name inputs, with checks to ensure they are strings.
"""


def say_my_name(first_name, last_name=""):
    """Print a full name in the format 'My name is
    <first name> <last name>'.

    Validates that first_name and last_name are strings.

    Args:
        first_name (str): The first name to print.
        last_name (str, optional): The last name to print. Defaults to "".

    Raises:
        TypeError: If first_name or last_name are not strings.

    Examples:
        >>> say_my_name("John", "Smith")
        My name is John Smith
        >>> say_my_name("Walter", "White")
        My name is Walter White
        >>> say_my_name("Bob ")
        My name is Bob
        >>> say_my_name(12, "White")
        Traceback (most recent call last):
        TypeError: first_name must be a string
        >>> say_my_name("John", 12)
        Traceback (most recent call last):
        TypeError: last_name must be a string
        >>> say_my_name(None, "Smith")
        Traceback (most recent call last):
        TypeError: first_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
