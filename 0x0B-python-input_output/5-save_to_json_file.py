#!/usr/bin/python3
"""
this module contains a function that obj to a text
file using json representaion
"""


def save_to_json_file(my_obj, filename):
    """
    function to write an obj file to a text file.
    an obj using json representation

    Parameter:
        @my_obj: python obj
        @filename: file to write to
    """
    import json
    with open(filename, 'w', encoding='utf-8') as fd:
        json.dump(my_obj, fd)
