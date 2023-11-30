#!/usr/bin/python3
"""
This module contains an empty class definition of a Rectangle
"""


class Rectangle():
    """
    This is a class instance of a rectangle

    class attributes:
        height
        width

    Methods:
        None
    """
    def __init__(self, width=0, height=0):
        """ 
        instance attributes:
            width
            height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ get and set width """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ get and set height """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
