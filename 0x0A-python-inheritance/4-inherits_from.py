#!/usr/bin/python3
"""
This module contains a class
"""


def inherits_from(obj, a_class):
    """
    this function checks for instance
    or subclass status

    Parameter:
        @obj: obj
        @a_class: class

    Return:
        true
        false, otherwise
    """
    if issubclass(obj, a_class):
        return True
    return False
