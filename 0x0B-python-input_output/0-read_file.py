"""This module handles a function that reads a file
"""


def read_file(filename=""):
    """Reads a file

    Args:
        filename (str, optional): file name. Defaults to "".
    """
    with open(filename, 'r', encoding="utf-8") as file:
        content = file.read()
        print("{}".format(content))
