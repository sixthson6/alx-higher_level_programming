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

    def update(self, *args, **kwargs):
        """method to update args and kwargs"""
        if len(args) is not None:
            if len(args) == 1:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        string = "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                   self.size)
        return string

    def to_dictionary(self):
        """print dict"""
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }
