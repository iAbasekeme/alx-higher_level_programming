#!/usr/bin/python3
"""This module holds a function that returns a list of available
attributes and methods of an object
"""


def lookup(obj):
    """This function returns the list of mthods and attributes

    Args:
        obj (list): list object
    """
    return dir(obj)
