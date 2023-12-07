#!/usr/bin/python3
"""
This module contains a function to return a simple data
structure for a json serialization of an obj
"""


def class_to_json(obj):
    """
    function to return dictionary description for json
    serialization

    Parameter:
        @obj: instance of a class

    Return:
        dictionary description
    """
    items = vars(obj)
    return items
