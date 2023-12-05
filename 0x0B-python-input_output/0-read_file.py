#!/usr/bin/python3
""" this module contains a function to open a file """


def read_file(filename=""):
    """
    function to open file

    Parameters:
        @filename: filename to be opened

    Return:
        contents of file
    """
    with open(filename, 'r', encoding='utf-8') as fd:
        file_content = fd.read()
        print(file_content)
