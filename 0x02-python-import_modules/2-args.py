#!/usr/bin/python3
import sys


def main():
    arguments = sys.argv

    if len(arguments) == 1:
        print("0 arguments:")
    elif len(arguments) == 2:
        print("1 argument")
        print("1: {}".format(arguments[1]))
    else:
        print("{} arguments:".format(len(arguments)))
    for arg_index in range(1, len(arguments)):
        print("{}: {}".format(arg_index, arguments[arg_index]))


if __name__ == '__main__':
    main()
