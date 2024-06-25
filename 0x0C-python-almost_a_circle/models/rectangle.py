#!/usr/bin/python3
"""empty class Rectangle that defines a rectangle"""
from .base import Base

class Rectangle(Base):
    """class Base"""
    __nb_objects=0
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Instantiation"""
        self__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super(id)
