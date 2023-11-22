#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        sum = a / b
        return (sum)
    except ZeroDivisionError:
        return (None)
