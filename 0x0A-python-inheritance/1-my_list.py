#!/usr/bin/python3
"""This module holds a function class MyList that inherits from list:
"""


class MyList(list):
    """This class inherits from a list class
    """

    def __init__(self):
        pass

    def print_sorted(self):
        """This functions prints the list but in a sorted order
        """
        sorted_list = self.copy()
        sorted_list.sort()
        print("{}".format(sorted_list))
