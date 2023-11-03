#!/usr/bin/python3
"""This module contains a function that prints a square
"""


def text_indentation(text):
    """This function prints a text with
    2 new lines after each of these characters: ., ? and :

    Args:
        text (str): Full Text

    Raises:
        TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    for i in text:
        print("{}".format(i), end='')
        if i in ['.', '?', ':']:
            print('\n\n', end='')
