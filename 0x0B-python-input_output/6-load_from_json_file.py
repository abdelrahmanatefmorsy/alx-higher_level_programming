#!/usr/bin/python3
""" module """


import json


def load_from_json_file(filename):
    """ json return dictionary """
    with open(filename, "r", encoding="UTF-8") as file:
        st = file.read()
        return json.loads(st)
