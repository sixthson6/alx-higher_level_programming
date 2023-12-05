#!/usr/bin/python3
""" this module contains a func to return
the JSON representation of an obj"""


def to_json_string(my_obj):
    """
    this function return the JSON representation
    of an obj

    Pararmeter:
        @my_obj: python obj
    """
    import json
    return json.dumps(my_obj)
