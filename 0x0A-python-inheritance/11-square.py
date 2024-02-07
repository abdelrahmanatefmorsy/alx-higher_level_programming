#!/usr/bin/python3
"""module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class that inherits from BaseGeometry"""

    def __init__(self, size):
        """intialize"""

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ area define """

        return self.__size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
