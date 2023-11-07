"""This modules holds a function that
writes an Object to a text file using JSON
"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a file in JSON

    Args:
        my_obj (object): obj
        filename (text file): file to write to
    """
    with open(filename, 'w') as file:
        to_json = json.dumps(my_obj)
        file.write(to_json)
