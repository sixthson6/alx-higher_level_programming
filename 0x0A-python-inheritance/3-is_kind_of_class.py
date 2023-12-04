#!/usr/bin/python3
"""
This module contains a class
"""


def is_kind_of_class(obj, a_class):
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
    if isinstance(obj, a_class):
        return True
    return False
