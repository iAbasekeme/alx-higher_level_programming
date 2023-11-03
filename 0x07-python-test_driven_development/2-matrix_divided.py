#!/usr/bin/python3
"""This module contains a function that divides
    all element of a matrix
"""


def matrix_divided(matrix, div):
    """This funxtion divided all elements of a matrix

    Args:
        matrix (int/float): list of integers/floats
        div (int/float): divisor

    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: Each row of the matrix must have the same size
        TypeError: div must be a number
        ZeroDivisionError: division by zero

    Returns: A new list all divided by the div
    """
    if not all(isinstance(row, list) and
               all(isinstance(sec_row, (int, float))
                   for sec_row in row) for row in matrix):
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats')

    first_row_size = len(matrix[0])
    for row in matrix:
        if len(row) != first_row_size:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_mztrix = []
    for row in matrix:
        new_row = []
        for sec_row in row:
            new_row.append(round(sec_row / div, 2))
        new_mztrix.append(new_row)
    return new_mztrix
