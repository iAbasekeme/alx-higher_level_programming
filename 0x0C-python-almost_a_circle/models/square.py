#!/usr/bin/python3
"""This is a square module that inherits from rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class square that inherits from rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Contructor for square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """A getter method for size
        """
        return self.width

    @size.setter
    def size(self, value):
        """A setter method
        """
        self.width = value
        self.height = value

    def __str__(self):
        """A str method to print to stdout
        """
        return f"[{self.__class__.__name__}]"\
               f" ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """An update method to update attribute of a class
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
                self.height = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]

        if kwargs:
            self.id = kwargs.get('id', self.id)
            self.width = kwargs.get('size', self.width)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)
