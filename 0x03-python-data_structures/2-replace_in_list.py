#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    x = len(my_list)
    if idx >= x or idx < 0:
        return (my_list)
    my_list[idx] = element
    return (my_list)
