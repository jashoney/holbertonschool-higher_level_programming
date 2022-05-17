#!/usr/bin/python3
""" defines a class Square """


class Square:
    """ instance for a Square """
    def __init__(self, size=0):
        """ initialise the instance """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """ function to calc an area of a square """
        return self.__size ** 2
