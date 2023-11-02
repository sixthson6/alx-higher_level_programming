#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

def main():
    a = 10
    b = 5

    _add = add(a, b)
    _sub = sub(a, b)
    _mul = mul(a, b)
    _div = div(a, b)

    print("{} + {} = {}".format(a, b, _add))
    print("{} - {} = {}".format(a, b, _sub))
    print("{} * {} = {}".format(a, b, _mul))
    print("{} / {} = {}".format(a, b, _div))

if __name__ == '__main__':
    main()
