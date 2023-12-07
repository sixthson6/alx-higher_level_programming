#!/usr/bin/python3
"""
this defines a file i/o function
"""


def append_after(filename="", search_string="", new_string=""):
    """
    open file, print 'new_string' after each line
    containing 'search_string'

    Parameters:
        @filename: file
        @search_string: search string
        @new_string: string to append
    """
    new = []
    with open(filename, 'r+', encoding='utf-8') as file:
        for line in file:
            new.append(line)
            if search_string in line:
                new.append(new_string)
    with open(filename, 'r+', encoding='utf-8') as file:
        file.writelines(new)
