#!/usr/bin/python3
"""
this module contains a function that appends
text to a file
"""


def append_write(filename="", text=""):
    """
    this file contains a file that appends text to
    an already existing file

    Parameters:
        @filename: file to be written to
        @text: text to append

    Return:
        number of chars added
    """
    with open(filename, 'a', encoding='utf-8') as fd:
        bytes_appended = fd.write(text)
    return bytes_appended
