#!/usr/bin/python3
""" this module contains a function

    function name:
        is_same_class
"""


def is_same_class(obj, a_class):
    """
    checks if an obj is an instance of a specified class

    Parameters:
        @obj: obj
        @a_class: class

    Return:
        True if obj is an instance of class
        False, otherwise
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
