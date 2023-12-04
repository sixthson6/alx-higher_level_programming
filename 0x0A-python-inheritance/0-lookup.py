#!/usr/bin/python3
"""
    This module contains a function to list all
    available attributes of any given object
"""


def lookup(obj):
    """
    function to list attributes and method of a class

    Parameters:
        @obj

    Return:
         a list of all attributes and methods of a class
    """
    return dir(obj)
