#!/usr/bin/python3
"""this module defines a class 'Base'"""


class Base:
    """this is a base class created to be
    inherited by other classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json string representation
        of objs"""
        import json
        return json.dumps(list_dictionaries)
