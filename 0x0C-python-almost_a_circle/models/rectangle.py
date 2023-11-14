#!/usr/bin/python3
"""A new module that inherits from Base class
"""
from models.base import Base


class Rectangle(Base):
    """A new rectangle class inheriting from base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor for square"""
        if not isinstance(width, int):
            raise TypeError('width must be an integer')

        if not isinstance(height, int):
            raise TypeError('height must be an integer')

        if not isinstance(x, int):
            raise TypeError('x must be an integer')

        if not isinstance(y, int):
            raise TypeError('y must be an integer')

        if width < 0:
            raise ValueError('width must be > 0')

        if height < 0:
            raise ValueError('height must be > 0')

        if x < 0:
            raise ValueError('x must be >= 0')

        if y < 0:
            raise ValueError('y must be >= 0')

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """A getter method for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """A setter method
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """A getter method for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """A setter method for height
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """A getter method for x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """A setter method for x
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """A getter method for y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """A setter method for y
        """
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """A public method for calculating area
        """
        return self.width * self.height

    def display(self):
        """A method that displays the Rectangle
            instance with the character # and also by
            taking care of x and y
        """
        for _ in range(self.y):
            print("{}".format(''))
        for _ in range(self.height):
            c = self.width
            print("{}".format(" " * self.x + '#' * c))

    def __str__(self):
        """A str method to print to stdout
        """
        return f"[{self.__class__.__name__}] "\
               f" ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """An update method to update attribute of a class
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]

        if kwargs:
            self.id = kwargs.get('id', self.id)
            self.width = kwargs.get('width', self.width)
            self.height = kwargs.get('height', self.height)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)
