#!/usr/bin/python3
""" this module contains a funtion to write to a file"""


def write_file(filename="", text=""):
    """
    this function writes to a file

    Parameters:
        @filename: name of file
        @text: input text

    Return: number of bytes written
    """
    with open(filename, 'w', encoding='utf-8') as fd:
        bytes_written = fd.write(text)
    return bytes_written
