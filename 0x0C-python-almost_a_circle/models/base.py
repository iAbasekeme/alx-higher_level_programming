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

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []

        obj_dicts = [obj.to_dictionary() for obj in list_objs]

        json_data = cls.to_json_string(obj_dicts)

        with open(f"{cls.__name__}.json", "w") as file:
            file.write(json_data)
