#!/usr/bin/python3
""" module """


def write_file(filename="", text=""):
    """ open file with with """

    with open(filename, "w", encoding="UTF-8") as file:
        """ print file """

        return file.write(text)
