#!/usr/bin/python3
""" Rectangle module. """


class Rectangle:
    """ class rectangle"""
    def __init__(self, width=0, height=0):
        """ Instantiation with optional width and height"""
        self.___width = width
        self.___height = height

    @property
    def width(self):
        """width
        """
        return self.___width

    @property
    def height(self):
        """height
        """
        return self.___height

    @width.setter
    def width(self, value):
        """width setter
        """
        if type(value) != int:
            raise ValueError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.___width = value

    @height.setter
    def height(self, value):
        """height setter
        """
        if type(value) != int:
            raise ValueError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.___height = value
