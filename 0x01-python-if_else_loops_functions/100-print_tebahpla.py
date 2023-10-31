#!/usr/bin/python3
i = 122
j = 89
k = 1
swp = i
while k <= 26:
    if k % 2 == 1:
        swp = i
        i = i - 2
    else:
        swp = j
        j = j - 2
    print(chr(swp), end="")
    k = k + 1
