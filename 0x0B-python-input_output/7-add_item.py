#!/usr/bin/python3
"""this module contains a scritpt to load and
save a json file from command line arguments
"""
import sys


if __name__ == '__main__':
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        objs = load_from_json_file("add_item.json")
    except FileNotFoundError:
        objs = []
    objs.extend(sys.argv[1:])
    save_to_json_file(objs, "add_item.json")
