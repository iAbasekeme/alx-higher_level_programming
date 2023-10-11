#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_row = []

    for row in matrix:
        matrix_col = []
        for i in row:
            matrix_col.append(i ** 2)
        matrix_row.append(matrix_col)
    return matrix_row
