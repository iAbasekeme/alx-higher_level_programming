#!/usr/bin/python3
"""A module that creates an object from a json file
"""
import json


def load_from_json_file(filename):
    """Creating an object from a JSOn file

    Args:
        filename (.txt): file
    """
    with open(filename, 'r')as file:
        load_json = json.load(file)
        return load_json
