#!/usr/bin/python3


import sys
from calculator_1 import add, sub, div, mul


def main():
    args = sys.argv
    if len(args) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(args[1])
    b = int(args[3])
    op = args[2]

    result = None

    if op == '+':
        result = add(a, b)
    elif op == '-':
        result = sub(a, b)
    elif op == '*':
        result = mul(a, b)
    elif op == '/':
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{} {} {} = {}".format(a, op, b, result))


if __name__ == '__main__':
    main()
