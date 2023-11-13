#!/usr/bin/pyhton3
"""This is a square module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class square that inherits from rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Contructor for square"""
        super().__init__(size, size, x, y, id)
