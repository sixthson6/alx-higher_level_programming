#!/usr/bin/python3
"""
module contains a fucn that computes
the pascal's triangle
"""


def pascal_triangle(n):
    """
    generate pascal's triangle of size n

    parameter:
        @n: size of triangle

    Return:
        list of integers representing triangle
    """
    if n <= 0:
        return []

    pascal = [[1]]
    while len(pascal) != n:
        t = pascal[-1]
        tmp = [1]
        for x in range(len(t) - 1):
            tmp.append(t[i] + t[i + 1])
        tmp.append(1)
        pascal.append(tmp)
    return pascal
