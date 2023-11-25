#!/usr/bin/python3
""" square module. """


class Square:
    """Empty class that defines a square."""
    def __init__(self, size=0):
        if type(size) != int:
            raise ValueError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        """intialize the attr"""
        self.__size = size

    def area(self):
        """Return area """
        return (self.__size * self.__size)
