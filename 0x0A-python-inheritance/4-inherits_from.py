#!/usr/bin/python3
"""This module holds a function that returns True
if the object is an instance of
a class that inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """a function that returns True if the object is an instance of
a class that inherited (directly or indirectly) from the specified class

    Args:
        obj (object): Object to be compared
        a_class (class): class
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
# This function uses the issubclass() function
# to check if the object's class (retrieved using type(obj))
# is a subclass of the
# specified class a_class. It also checks if the object's
# class is not exactly the
# same as a_class (using type(obj) is not a_class)
# to ensure that it's not an instance of the specified class itself.
