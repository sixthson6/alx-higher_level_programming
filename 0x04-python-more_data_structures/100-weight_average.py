#!/usr/bin/python3
def weight_average(my_list=[]):
    total = total2 = 0
    for i in range(len(my_list)):
        total += my_list[i][-1] * my_list[i][-2]
        total2 += my_list[i][-1]
    result = total/total2
    return result
