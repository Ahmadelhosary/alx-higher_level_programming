#!/usr/bin/python3
def matrix_divided(matrix, div):
    result = []

    # Divide each element in the matrix by the divisor
    for row in matrix:
        new_row = [element / div for element in row]
        result.append(new_row)
