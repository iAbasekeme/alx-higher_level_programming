"""A new class
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """New class
    """

    def __init__(self, size):
        """New Method
        """
        super().__init__(size, size)
