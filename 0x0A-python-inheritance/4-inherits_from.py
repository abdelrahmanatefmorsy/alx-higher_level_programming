#!/usr/bin/python3
""" module line """


def inherits_from(obj, a_class):
    """ check """

    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    return False
