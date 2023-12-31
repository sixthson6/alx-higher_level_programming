#!/usr/bin/python3
"""
module containg text_indentation() function

"""


def text_indentation(text):
    """
    function prints 2 new after ".?:"

    return:
        Nothing
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    sig = text[:]

    for deli in ".?:":
        text_list = sig.split(deli)
        sig = ""
        for i in text_list:
            i = i.strip(" ")
            sig = i + deli if sig is "" else sig + "\n\n" + i + d
    print(sig[:-3], end="")
