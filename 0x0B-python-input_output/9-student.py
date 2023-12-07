#!/usr/bin/python3
"""
this module contains a class
"""


class Student:
    """
    this class describes a student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        retrieve dictionary repr of instance
        """
        return vars(self)
