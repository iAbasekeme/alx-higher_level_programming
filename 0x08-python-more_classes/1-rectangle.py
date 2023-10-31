#!/usr/bin/python3
"""This module creates a new Rectangle class
"""


class Rectangle:
    """This is a rectangle class
    """

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """This getter method returns the Rectangle width data"""
        return self.__width

    @width.setter
    def width(self, value):
        """This is a setter method"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This instance method return the current Rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise Exception("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
