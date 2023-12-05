#!/usr/bin/python3
"""this module contain a func that returns
an obj repr by a json string"""


def from_json_string(my_str):
    """
    function returns an obj(python data structure)
    represented by a json string

    Parameter:
        @my_str: json string
    """
    import json
    return json.loads(my_str)
