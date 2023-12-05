#!/usr/bin/python3
""" this module contains a function to open a file """


def read_file(filename=""):
    with open(filename, 'r', encoding='utf-8') as fd:
        file_content = fd.read()
        print(file_content)
