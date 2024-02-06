#!/usr/bin/python3
""" module """


import json


def from_json_string(my_str):
    """ json return dictionary """

    return json.load(my_str)
