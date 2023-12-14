#!/usr/bin/python3
""" this module define a class Rectangle """
from models.base import Base


class Rectangle(Base):
    """
    this class define a Rectangle

    Attrs:
        width
        height
        x
        y

    Exceptions:
        TypeError if type is not int
        ValueError if height and width are not >= 0
        ValueError if x and y are not > 0
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """get width using getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width using setter method

        Exceptions
            TypeError
            ValueError
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        get height
        using getter method
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        set height using setter method

        Exceptions
            TypeError
            ValueErrr
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get x using getter method"""
        return self.__x

    @x.setter
    def x(self, value):
        """
        set x using setter method

        Exceptions:
            ValueError
            TypeError
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        get y
        using getter method
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        set y using setter method

        Exceptions:
            ValueError
            TypeError
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        calculate area of rectangle

        args:
            width
            retangle
        """
        return self.__width * self.__height

    def display(self):
        """
        print the rectangle instance
        using '#'
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + '#' * self.__width)

    def __str__(self):
        string = "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                         self.__x,
                                                         self.__y,
                                                         self.__width,
                                                         self.__height)
        return string

    def update(self, *args, **kwargs):
        """
        update the instance attributes

        width
        height
        x
        y
        """
        if len(args) != None:
            if len(args) == 1:
                self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]
        for k, v in kwargs.items():
            setattr(self, k, v)
