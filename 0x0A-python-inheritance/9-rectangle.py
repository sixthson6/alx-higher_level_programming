#!/usr/bin/python3
"""
this module contains a class 'Rectangle'
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    this class inherits BaseGeometry
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        string = "[Rectangle] {}/{}".format(self.__width, self.__height)
        return string
