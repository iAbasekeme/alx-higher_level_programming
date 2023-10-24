#!/usr/bin/python3
"""This is a module that defines a module base on 1-square"""


class Square:
    """This is a class that initializes
    an instance of the Square class and raises errors
    if the size is 0 or size is not int"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
