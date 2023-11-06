#!/usr/bin/python3

def max_integer(my_list=[]):
    mx = 0
    if len(my_list) == 0:
        return
    for i in range(len(my_list)):
        if my_list[i] > mx:
            mx = my_list[i]
    return mx
