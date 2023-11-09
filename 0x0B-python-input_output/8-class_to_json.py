#!/usr/bin/python3

"""Class to JSON
"""


def class_to_json(obj):
    """a function that returns the dictionary description with simple
    data structure (list, dictionary,
    string, integer and boolean) for JSON serialization of an object:

    Args:
        obj (class): object
    """
    ty_obj = type(obj)

    if ty_obj in (str, int, bool):
        result = ty_obj

    elif ty_obj is list:
        result = [class_to_json(elem) for elem in obj]

    elif ty_obj is dict:
        result = {key: class_to_json(value) for key, value in obj.items()}

    elif hasattr(obj, '__dict__'):
        result = {key: class_to_json(value)
                  for key, value in obj.__dict__.items()}

    return result
