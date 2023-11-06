#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    x = len(tuple_a)
    y = len(tuple_b)
    sum1 = 0
    sum2 = 0
    if x == 1:
        sum1 += tuple_a[0]
    elif x > 1:
        sum1 += tuple_a[0]
        sum2 += tuple_a[1]
    if y == 1:
        sum1 += tuple_b[0]
    elif y > 1:
        sum1 += tuple_b[0]
        sum2 += tuple_b[1]
    tub = (sum1, sum2)
    return (tub)
