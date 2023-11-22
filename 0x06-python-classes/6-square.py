#!/usr/bin/python3
""" Square Class"""


class Square():
    """
    An empty 'Square class'
    """
    def __init__(self, size=0, position=(0, 0)):
        """ instance attributes """
        if not type(size) == int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size
        self._position = position

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

    @property
    def position(self):
        return self._position

    @position.setter
    def postion(self, value):
        if not type(value) == tuple or len(value) != 2:
            if not all(isinstance(x, int) and x >= 0 for x in value):
                str = "position must be a tuple of 2 positive integers"
                raise TypeError(str)
        self._position = value

    def my_print(self):
        """ print square in '#' """
        if self._Square__size == 0:
            print()
        for i in range(self.postion[1]):
            print("")
        for i in range(self._Square__size):
            print(" " * self.position[0], end='')
            print("#" * self._Square__size)
