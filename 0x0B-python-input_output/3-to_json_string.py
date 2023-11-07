#!/usr/bin/python3
"""This module holds a function that returns the json of an object
"""
import json


def to_json_string(my_obj):
    """This function returns the json rep of an object

    Args:
        my_obj (_type_): Any
    """
    return json.dumps(my_obj)
