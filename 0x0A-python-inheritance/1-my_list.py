#!/usr/bin/python3
""" module line """


class MyList(list):
    """ class dervived from list"""
    pass

    def print_sorted(self):
        """print the sorted list"""

        print(sorted(list(self)))
