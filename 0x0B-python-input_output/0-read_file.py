#!/usr/bin/python3
""" module """


def read_file(filename=""):
    """ open file with with """

    with open(filename, "r", encoding="utf-8") as file:
        """ print file """

        print(file.read())
