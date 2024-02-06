#!/usr/bin/python3
""" module """


def write_file(filename="", text=""):
    """ open file with with """

    with open(filename, "w", encoding="UTF-8") as file:
        """ print file """

        file.write(text)
    x = len(text)
    for i in text:
        if i == ' ' or i == '\n':
            x = x + 1
    return (x)
