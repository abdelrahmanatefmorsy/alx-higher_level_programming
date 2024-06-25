#!/usr/bin/python3
"""empty class Rectangle that defines a rectangle"""
from .base import Base


class Rectangle(Base):
    """class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Instantiation"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """getter"""
        return self.__width

    @property
    def height(self):
        "getter"
        return self.__height

    @width.setter
    def width(self, width):
        """setter"""
        self.validate_integer(self,"width",width,False)
        self.__width = width

    @height.setter
    def height(self, height):
        """setter"""
        self.validate_integer(self,"height",height,False)
        self.__height = height

    @property
    def x(self):
        '''x of this rectangle.'''
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_integer("x", value)
        self.__x = value
    @property
    def y(self):
        '''y of this rectangle.'''
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name, value, eq=True):
        '''Method for validating the value.'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))
    
    def area(self):
        return self.__width * self.__height
