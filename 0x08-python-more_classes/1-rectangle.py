#!/usr/bin/python3
""" Rectangle module. """


class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.___width

    @property
    def height(self):
        return self.___height

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise ValueError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.___width = value

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise ValueError("height must be an integer")
        if value < 0:
            raise ValueError("def __init__(self, width=0, height=0):")
        self.___height = value
