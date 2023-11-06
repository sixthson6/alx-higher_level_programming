#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == "":
        return (None)
    else:
        for num in my_list:
            if my_list[num] > my_list[num + 1]:
                return (my_list[num])
