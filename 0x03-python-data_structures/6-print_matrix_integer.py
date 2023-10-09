#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            if row:
                for num in row:
                    if num < 0:
                        print("{:d}".format(num), end=" ")
                    else:
                        print("{:d}".format(num), end=" ")
            print()
