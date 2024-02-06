#!/usr/bin/python3
""" module """


import json


def save_to_json_file(my_obj, filename):
    """ json return dictionary """

    with open(filename, "w", encoding="UTF-8") as file:
        file.write(json.dumbs(my_obj))
