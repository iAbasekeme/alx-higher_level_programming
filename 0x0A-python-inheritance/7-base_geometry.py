#!/usr/bin/python3
"""This is amodule that holds a new class
"""


class BaseGeometry:
    """This ia an empty class name BaseGeometry
    """

    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
