#!/usr/bin/python3
i = ", "
for x in range(0, 100):
    if x == 99:
        i = "\n"
    if x < 10:
        print("0{}{}".format(x, i), end="")
    else:
        print("{}{}".format(x, i), end="")
