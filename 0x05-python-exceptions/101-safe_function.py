#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    exe = None
    try:
        exe = fct(*args)
    except Exception as x:
        sys.stderr.write("Exception: {}\n".format(x))
    else:
        return None
    return exe
