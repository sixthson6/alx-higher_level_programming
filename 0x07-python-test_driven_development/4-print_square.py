#!/usr/bin/python3
"""
contains print_square() fucntion
"""


def print_square(size):
    """
    function that print a square of size with '#'

    Return:
        Nothing
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
