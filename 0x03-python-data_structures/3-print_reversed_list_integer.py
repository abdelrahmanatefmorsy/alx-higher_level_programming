#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    lst = my_list[:]
    lst.reverse()
    for i in range(len(lst)):
        print("{:d}".format(lst[i]))
