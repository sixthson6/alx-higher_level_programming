#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
    except Exception as x:
        sys.stderr.write("Exception: {}".format(x))
        return False
    else:
        return True
