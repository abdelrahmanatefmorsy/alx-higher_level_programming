#!/usr/bin/python3
""" square module. """


class Square:
    """Empty class that defines a square."""
    def __init__(self, size=0):
        """intialize values"""
        self.__size = size

    @property
    def size(self):
        """Getter method"""
        return self.__size

    @size.setter
    def size(self, size):
        """setter method"""
        if type(size) != int:
            raise ValueError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return value"""
        return (self.__size * self.__size)
