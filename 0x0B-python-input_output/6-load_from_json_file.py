#!/usr/bin/python3
"""this module contains a function that
creates an obj from a json file
"""


def load_from_json_file(filename):
    """
    load data form a json file

    Parameter:
        @filename: json file

    """
    import json
    with open(filename, 'r', encoding='utf-8') as fd:
        json_file = fd.read()
        obj = json.loads(json_file)
    return obj
