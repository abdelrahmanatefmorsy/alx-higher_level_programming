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

    def area(self):
        return self.___width * self.___height

    def perimeter(self):
        if self.___width == 0 or self.___height == 0:
            return (0)
        else:
            return (2 * (self.___width + self.___height))

    def __str__(self):
        """ return the rectangle with the character #
        """
        if self.__width is 0 or self.__height is 0:
            return ""
        return ("\n".join(["".join(["#" for i in range(self.__width)])
                for j in range(self.__height)]))