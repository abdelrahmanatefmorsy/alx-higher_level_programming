#!/usr/bin/python3
"""empty class Rectangle that defines a rectangle"""
class Base:
    """class Base"""
    __nb_objects=0
    def __init__(self, id=None):
        """ Instantiation"""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects+=1
            self.id=Base.__nb_objects
