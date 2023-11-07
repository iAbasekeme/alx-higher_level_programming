"""This module holds a functio that appends to a file
"""


def append_write(filename="", text=""):
    """A function that appends to a file

    Args:
        filename (str, optional): Name of the file. Defaults to "".
        text (str, optional): Appendant. Defaults to "".
    """
    with open(filename, 'a', encoding="utf-8") as file:
        content = file.write(text)
        return content
