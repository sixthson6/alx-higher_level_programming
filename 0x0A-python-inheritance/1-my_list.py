#!/usr/bin/python3
"""
This module contains a class that inherits 'list'
"""


class MyList(list):
    """
        This is a class

        Attributes:
            None

        Methods:
            print_sorted()
    """
    def __init__(self):
        """ obj instance attrubutes == NULL """
        pass

    def print_sorted(self):
        """ method to print lists """
        print(sorted(self))
