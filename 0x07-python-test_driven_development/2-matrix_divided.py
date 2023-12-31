#!/usr/bin/python3
"""
this module contains that divides all elements of a matrix

Function:
    matrix_divided()
"""


def matrix_divided(matrix, div):
    """
    divide every element of the matrix with a number

    Return:
        divided matrix
    """
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    message = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix or not isinstance(matrix, list):
        raise TypeError(message)
    length = 0
    message_t = "Each row of the matrix must have the same size"

    for ele in matrix:
        if not ele or not isinstance(ele, list):
            raise TypeError(message)
        if length != 0 and len(ele) != length:
            raise TypeError(message_t)
        for number in ele:
            if not type(number) in (int, float):
                raise TypeError(message)

        length = len(ele)

    man = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (man)
