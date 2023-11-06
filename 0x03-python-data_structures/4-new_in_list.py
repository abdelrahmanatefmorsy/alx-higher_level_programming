#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    b = my_list
    x = len(my_list)
    if idx >= x or idx < 0:
        return (my_list)
    b[idx] = element
    return (b)
