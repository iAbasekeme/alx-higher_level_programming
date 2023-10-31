#!/usr/bin/python3
"""This module contains a functions that adds two integers
"""


def add_integer(a, b=98):
    """This functions adds two integers

    Args:
        a (int or float): First Argument
        b (int or float, optional): second Argument. Defaults to 98.

    Raises:
    TypeError: a must be an integer
    TypeError: b must be an integer

    Returns:
    int: result of te addition
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
