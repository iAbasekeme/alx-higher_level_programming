#!/usr/bin/python3
"""This module holds a a function that returns True if the object
    is exactly an instance of the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """This function returns True or false for
    a comparison of class and instance

    Args:
        obj (instance): instance of the class
        a_class (class): class
    """
    return type(obj) is a_class
