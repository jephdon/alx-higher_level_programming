#!/usr/bin/python3
"""A module containing a function to find a peak
in a list of integers.
"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers.

    A peak is an element that is not smaller than its neighbors.
    The function uses a binary search approach to achieve
    O(log n) complexity.

    Args:
        list_of_integers (list): A list of integers.

    Returns:
        int or None: A peak element from the list, or None if
        the list is empty.
    """
    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
