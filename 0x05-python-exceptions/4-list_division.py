#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list_3 = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            if result != result or result == float('inf') or result == float('-inf'):
                resul = 0.0
        except IndexError:
            print("out of range")
            result = 0.0
        except ZeroDivisionError:
            print("division by 0")
            result = 0.0
        except TypeError:
            print("wrong type")
            result = 0.0
        my_list_3.append(result)
    return my_list_3

