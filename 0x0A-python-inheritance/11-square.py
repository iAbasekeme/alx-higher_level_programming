#!/usr/bin/python3
""" class module
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """New class
    """

    def __init__(self, size):
        """New Method
        """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """custom str method for print the rectangle"""
        return f"[Square] {self.__size}/{self.__size}"
