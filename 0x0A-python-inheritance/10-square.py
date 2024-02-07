#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

"""
===================================
module with class square
===================================
"""


class Square(Rectangle):
    """square class that inherits from BaseGeometry"""

    def __init__(self, size):
        """intialize"""

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ area define """

        return self.__size ** 2
