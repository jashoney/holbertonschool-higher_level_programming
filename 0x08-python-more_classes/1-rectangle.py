#!/usr/bin/python3
""" defining a class Rectangle """


class Rectangle:
    """ defining a class Rectangle """
    def __init__(self, width=0, height=0):
        """ instantiation method """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ width getter """
        return self.__width

    @property
    def height(self):
        """ height getter """
        return self.__height

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
