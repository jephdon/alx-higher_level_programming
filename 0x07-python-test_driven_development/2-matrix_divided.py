#!/usr/bin/python3
"""A module for dividing all elements in a matrix by a number.

This module provides a function that divides each element in a
matrix by a given divisor, returning a new matrix with rounded
results. It includes validation for matrix structure and divisor type.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a number and return a new matrix.

    Each element in the matrix is divided by div and rounded to 2
    decimal places.

    Args:
        matrix (list of lists): A matrix (list of lists) of integers
        or floats.
        div (int or float): The divisor to divide each element by.

    Returns:
        list of lists: A new matrix with divided and rounded elements.

    Raises:
        TypeError: If matrix is not a list of lists of ints/floats,
        or if rows have different sizes, or if div is not a number.
        ZeroDivisionError: If div is 0.

    Examples:
        >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
        [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
        >>> matrix_divided([[1.5, 2.5], [3.5, 4.5]], 0.5)
        [[3.0, 5.0], [7.0, 9.0]]
    """
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for elem in row:
            new_value = round(elem / div, 2)
            new_row.append(new_value)
        new_matrix.append(new_row)
    return new_matrix
