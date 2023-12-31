#!/usr/bin/python3
""" contains a function that adds two numbers """


def add_integer(a, b=98):
    """
    function adds two numbers

    Return:
        sum of a and b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
