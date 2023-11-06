#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if type(my_list) is list:
        lst = my_list[:]
        lst.reverse()
        for i in range(len(lst)):
            print("{:d}".format(lst[i]))
