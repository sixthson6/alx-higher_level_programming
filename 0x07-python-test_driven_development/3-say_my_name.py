#!/usr/bin/python3
"""
this module conatains the function

say_my_name()
"""


def say_my_name(first_name, last_name=""):
    """
    function print out first name and last name

    return:
        string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
