#!/usr/bin/python3
"""
this moduel conatains only a func
"""


def add_attribute(obj, attr, value):
    """
    func adds new attribute to obj

    parameters:
        @obj: object
        @attr: attribute to be added
        @value: corresponding value

    Return: Nada!
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
