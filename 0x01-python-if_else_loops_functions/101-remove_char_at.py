#!/usr/bin/python3
def remove_char_at(str, n):
    if (n < 0):
        return (str)
    str2 = str[:n]
    str3 = str[n + 1:]
    return (str2 + str3)
