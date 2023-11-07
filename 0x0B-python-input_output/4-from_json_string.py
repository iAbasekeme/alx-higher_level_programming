#!/usr/bin/python3
"""This module holds a function that
returns obj represented by JSON
"""
import json


def from_json_string(my_str):
    """Returns the an obj from JSON

    Args:
        my_str (string): String to be converted
    """
    return json.loads(my_str)
