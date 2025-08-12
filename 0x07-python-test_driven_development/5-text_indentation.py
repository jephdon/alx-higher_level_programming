#!/usr/bin/python3
"""A module for indenting text with new lines after specific characters.

This module provides a function that prints text with 2 new lines after
each '.', '?', or ':', with validation for string input and no
leading/trailing spaces on lines.
"""


def text_indentation(text):
    """Print text with 2 new lines after each '.', '?', or ':'.

    Validates that text is a string. Trims spaces at the beginning
    and end of each printed line.

    Args:
        text (str): The text to print with indentation.

    Raises:
        TypeError: If text is not a string.

    Examples:
        >>> text_indentation("Hello. World? This: is a test.")
        Hello$
        $
        World$
        $
        This$
        $
        is a test
        >>> text_indentation("")

        >>> text_indentation(None)
        Traceback (most recent call last):
        TypeError: text must be a string
        >>> text_indentation("Leading space. Trailing space ")
        Leading space$
        $
        Trailing space
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Replace special chars with the char + two new lines
    special_chars = ".?:"
    for char in special_chars:
        text = text.replace(char, char + "\n\n")

    # Split the text into lines and strip leading/trailing spaces
    lines = text.splitlines()
    for line in lines:
        print(line.strip())
