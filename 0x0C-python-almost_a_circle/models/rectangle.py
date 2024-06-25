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
        self.validate_integer("width",width,False)
        self.__width = width

    @height.setter
    def height(self, height):
        """setter"""
        self.validate_integer("height",height,False)
        self.__height = height

    @property
    def x(self):
        '''x of this rectangle.'''
        return self.__x

    @x.setter
    def x(self, value):
        """x of rec"""
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
        """return  area """
        return self.__width * self.__height
    
    def display(self):
        """display"""
        for i in range(0,self.__height):
            for j in range(0,self.__width):
                print("#",end="")
            print("")
    def __str__(self):
        """str"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)
    
    def update(self, *args):
        """update"""
        if len(args)>=1 and args[0] is not None:
            self.id = args[0]
        if len(args)>=2 and args[1] is not None:
            self.__width = args[1]
        if len(args)>=3 and args[2] is not None:
            self.__height = args[2]
        if len(args)>=4 and  args[3] is not None:
            self.__x = args[3]
        if len(args)>=5 and args[4] is not None:
            self.__y = args[4]
