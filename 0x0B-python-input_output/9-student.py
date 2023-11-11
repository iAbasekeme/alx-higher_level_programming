#!/usr/bin/python3
"""A module that holds class Student that defines a student by:
"""


class Student:
    """A student class
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """FUnction to return a dict

        Returns:
            dict: dictionary for instance
        """
        return self.__dict__
