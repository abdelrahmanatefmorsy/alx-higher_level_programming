#!/usr/bin/python3
"""module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class that inherits from BaseGeometry"""

    def __init__(self, size):
        """intialize"""

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ area define """

        return self.__size ** 2

    def __str__(self):
        """ str method """
        return "[Square] {}/{}".format(self.__size, self.__size)
