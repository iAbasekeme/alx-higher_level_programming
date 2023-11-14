#!/usr/bin/python3
"""A new module for a class Base
"""
import json


class Base:
    """A Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor

        Args:
            id (class, optional): public instance . Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string
        representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
