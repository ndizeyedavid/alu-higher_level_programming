#!/usr/bin/python3
"""Module that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div and returns a new matrix.

    Args:
        matrix: list of lists of integers or floats
        div: number (integer or float) to divide by

    Returns:
        list: new matrix with elements divided by div, rounded to 2 decimals

    Raises:
        TypeError: if matrix is not a list of lists of ints/floats,
                   if rows have different sizes, or if div is not a number
        ZeroDivisionError: if div is 0
    """
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    if not all(isinstance(x, (int, float)) for row in matrix for x in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    row_size = len(matrix[0]) if matrix else 0
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if isinstance(div, float):
        if div != div or div == float('inf') or div == float('-inf'):
            raise TypeError("div must be a number")
    return [[round(x / div, 2) for x in row] for row in matrix]
