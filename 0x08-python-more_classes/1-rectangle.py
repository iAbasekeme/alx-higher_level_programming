#!/usr/bin/python3
"""This module creates a new Rectangle class
"""


class Rectangle:
    """This is a rectangle class
    """

    def __init__(self, width=0, height=0):
        """The init method that initializes each time an
            instance is created

        Args:
            width (int, optional): width of the rectangle. Defaults to 0.
            height (int, optional): height of the rectangle. Defaults to 0.

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """This getter method returns the Rectangle width data"""
        return self.__width

    @property
    def height(self):
        """This instance method return the current Rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """This is a setter method"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
