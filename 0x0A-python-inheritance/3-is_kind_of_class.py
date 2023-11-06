#!/usr/bin/python3
"""A function that returns True if the object is an instance of
or if the object is an instance of a class that inherited
from, the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """This function returns True or false if an object is an instance 

    Args:
        obj (obj): object
        a_class (class): class
    """
    return isinstance(obj, a_class)
