#!/usr/bin/python3

import sys

def add_infinite(*args):
    result = 0
    for i in range(len(args) -1):
        result += args[i] + args[i + 1]
    return (result)

def main():
    result = add_infinite(*map(int, sys.argv[1:]))
    print("{}".format(result))

if __name__ == '__main__':
    main()
