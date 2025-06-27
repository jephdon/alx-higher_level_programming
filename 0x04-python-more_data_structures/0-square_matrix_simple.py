#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Create an empty list for the new matrix
    new_matrix = []
    # Loop through each row in the input matrix
    for row in matrix:
        # Create an empty list for the new row
        new_row = []
        # Loop through each number in the row
        for num in row:
            # Square the number and add it to the new row
            new_row.append(num ** 2)
        # Add the completed new row to the matrix
        new_matrix.append(new_row)
    return new_matrix
