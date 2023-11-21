#!/usr/bin/python3
def raise_exception():
    variable = None
    try:
        variable += 1
    except TypeError as error:
        raise type(error)
