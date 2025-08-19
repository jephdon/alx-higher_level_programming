#!/usr/bin/python3
"""A module for a custom list class that inherits from list.

This module provides MyList, a subclass of list
with a print_sorted method.
"""


class MyList(list):
    """A subclass of list with a method to print the list in sorted order.

    This class inherits all behavior from list and adds print_sorted.
    """

    def print_sorted(self):
        """Print the list in ascending sorted order.

        Assumes all elements are integers. Does not
        modify the original list.
        """
        sorted_list = sorted(self)
        print(sorted_list)
