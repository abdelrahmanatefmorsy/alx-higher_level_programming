#!/usr/bin/python3
""" square module. """


class Square:
    """Empty class that defines a square."""
    def __init__(self, size=0, position=(0, 0)):
        """intialize values"""
        self.__size = size
        self.position = position

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

    def my_print(self):
        """ print method"""
        if self.__size == 0:
            print()
        else:
            for y in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(' ', end='')
                for j in range(self.__size):
                    print('#', end='')
                print()

    @property
    def position(self):
        """Gender method"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter method"""
        if type(value) != tuple or len(value) != 2:
            raise ValueError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value
