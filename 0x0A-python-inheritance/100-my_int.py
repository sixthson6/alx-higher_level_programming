#!/usr/bin/python3
""" this module contains a class """


class MyInt(int):
    """ inverts equal sign operator """
    def __eq__(self, value):
        return self.real != value

    def __ne__(self, value):
        return self.real == value
