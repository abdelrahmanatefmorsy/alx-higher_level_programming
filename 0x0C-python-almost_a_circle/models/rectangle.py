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
        self.__width = width

    @height.setter
    def height(self, height):
        """setter"""
        self.__height = height
