#!/usr/bin/python3
"""This module contains a function that prints a square
"""


def print_square(size):
    """A function that prints a square with the character #

    Args:
        size (str): size is the size length of the square

    Raises:
        TypeError: 'size must be an integer'
        ValueError: 'size must be >= 0'
        TypeError: 'size must be an integer'
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')

    for _ in range(size):
        print("{}".format(size * '#'))
