#!/usr/bin/python3
"""
this module only contains a class
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    this class inherits Rectangle
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        string = "[Square] {}/{}".format(self.__size, self.__size)
        return string
