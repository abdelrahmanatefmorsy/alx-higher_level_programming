#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    b = my_list[:]
    x = len(my_list)
    for i in range(x):
        if my_list[i] % 2 == 0:
            b[i] = True
        else:
            b[i] = False
    return (b)
