"""This module handles a function that reads a file
"""


def read_file(filename=""):
    """Reads a file

    Args:
        filename (str, optional): file name. Defaults to "".
    """
    with open(filename, 'r') as file:
        content = file.read()
        print(f"{content}")
