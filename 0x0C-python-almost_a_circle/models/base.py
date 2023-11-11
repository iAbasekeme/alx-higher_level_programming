#!/usr/bin/python3
"""A new module for a class Base
"""


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
