#!/usr/bin/python3
#!/usr/bin/python3
"""This is a module that defines a module base on 2-square"""


class Square:
    """This is a class that initializes
    an instance of the Square class and raises errors
    if the size is 0 or size is not int"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """This getter method returns the current data"""
        return self.__size

    @size.setter
    def size(self, value):
        """This is a setter method"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2
