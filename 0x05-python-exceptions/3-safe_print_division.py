#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        sum = a / b
    except ZeroDivisionError:
        sum = 0
    print("Inside result: {:d}".format(sum))
    return (sum)
