#!/usr/bin/python3
"""This is a module that writes a class square """


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
        """This instance method return the current square method"""
        print(self.__size ** 2)

    def my_print(self):
        """A public instance method that prints in
        stdout the square with the character #"""
        if self.size == 0:
            print("")
        else:
            for _ in range(self.size):
                # this prints (#) self.size times for each run
                print("{}".format("#"*self.size))
