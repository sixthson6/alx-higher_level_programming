#!/usr/bin/python3
""" this module contains a function to open a file """


def read_file(filename=""):
    with open(filename, 'r') as fd:
        for line in fd:
            print(line)
