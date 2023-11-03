#!/usr/bin/python3
"""This module contains a file that prints a first and last name of a person
"""


def say_my_name(first_name, last_name=""):
    """ This function reads two names and returns them

    Args:
        first_name (str): Person First name
        last_name (str, optional): Person Last name. Defaults to "".

    Raises:
        TypeError: first_name must be a string or last_name must be a string
    """
    if not (isinstance(first_name, str) or (isinstance(last_name, str))):
        raise TypeError(
            'first_name must be a string or last_name must be a string')
    print("My name is {:s} {:s}".format(first_name, last_name))
