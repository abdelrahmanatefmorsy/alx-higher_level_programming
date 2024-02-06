#!/usr/bin/python3
"""module"""


class Student:
    """define new class"""
    def __init__(self, first_name, last_name, age):
        """intialize"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs):
        """return dict"""

        try:
            for i in attrs:
                if type(i) != str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        mylist = dict()
        for i, j in self.__dict__.items():
            if i in attrs:
                mylist[i] = j
        return mylist
