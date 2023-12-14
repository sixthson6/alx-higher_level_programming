#!/usr/bin/python3
"""this module defines a square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    this class defines a square class

    Attrs:
        size
        x
        y
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get size using getter property"""
        return self.width

    @size.setter
    def size(self, value):
        """set size using setter property"""
        self.width = value
        self.height = value

    def __str__(self):
        string = "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                   self.size)
        return string
