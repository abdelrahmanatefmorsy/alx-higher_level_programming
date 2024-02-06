#!/usr/bin/python3
""" module """

def read_file(filename=""):
    """ open file with with """

    with open(filename, "r") as file:
        print(file.read())
