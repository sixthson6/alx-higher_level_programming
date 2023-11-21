#!/usr/bin/python3
""" Square Class"""


class Square():
    """
    An empty 'Square class'
    """
    def __init__(self, size=0):
        """ instance attributes """
        if not type(size) == int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size

    def area(self):
        """ area method """
        return self._Square__size ** 2

    @property
    def size(self):
        return self._Square__size

    @size.setter
    def size(self, value):
        if not type(value) == int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value

    def my_print(self):
        """ print square in '#' """
        if self._Square__size == 0:
            print()
        for i in range(self._Square__size):
            for j in range(self._Square__size):
                print("#", end='')
            print()
