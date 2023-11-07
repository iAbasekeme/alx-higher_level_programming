"""This module hold sa function that wrotes to a file
"""


def write_file(filename="", text=""):
    """Writes to a file

    Args:
        filename (str, optional): file to write to. Defaults to "".
        text (str, optional): Text to be written. Defaults to "".
    """
    with open('filename.txt', 'w', encoding="utf-8") as file:
        content = file.write(text)
        return content
