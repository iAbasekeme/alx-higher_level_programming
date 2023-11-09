#!/usr/bin/python3
"""full rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A subclass of a superclass

    Args:
        BaseGeometry (class): A class that validates it's attributes
    """

    def __init__(self, width, height):
        """A constructor function that validates a height
        and width of a rectangle

        Args:
            width (int): Width
            height (int): Height
        """
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height

        def __str__(self):
            """custom str method for print the rectangle"""
            return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)

        def area(self):
            """computes area of the retangle"""
            return self.__height * self.__width
