#!/usr/bin/python3
""" module """


def append_write(filename="", text=""):
    """ open file with with """

    with open(filename, "a", encoding="UTF-8") as file:
        """ print file """

        return file.write(text)
