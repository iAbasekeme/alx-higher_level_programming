#!/usr/bin/python3
"""This module creates a new Rectangle class
"""


class Rectangle:
    """This is a rectangle class
    """
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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

    def area(self):
        """An instance method tat calculates the area of a rectangle

        Returns:
            int: The area of the recttangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """This method calculates and return the
        perimeter of a rectangle

        Returns:
            int: Perimeter of a rectangle
        """
        if self.__width and self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            ty = ''
            for i in range(self.__height):
                ty += str(self.print_symbol) * self.__width
                if i != self.__height - 1:
                    ty += '\n'
            return ty

    def __repr__(self):
        """This function prints a string in repr format
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """This function performs a delete operation
        """
        Rectangle.number_of_instances -= 1
        print("{:s}".format('Bye rectangle...'))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        rect1 = rect_1.width * rect_1.height
        rect2 = rect_2.width * rect_2.height

        if rect1 is rect2:
            return rect_1

        mx = max(rect1, rect2)

        if mx == rect1:
            return rect_1
        else:
            return rect_2
