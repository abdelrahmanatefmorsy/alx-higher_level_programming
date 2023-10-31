#!/usr/bin/python3
i = 122
j = 89
k = 1
while k <= 26:
    if k % 2 == 1:
        print(chr(i), end="")
        i = i - 2
    else:
        print(chr(j), end="")
        j = j - 2
    k = k + 1
