#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return None
    for row in matrix:
        for num in row:
            print("{}".format(num), end=" ")
        print()
