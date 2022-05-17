#!/usr/bin/python3
""" defines a class square """


class Square:
    """ sets aup a square instance """
    def __init__(self, size=0):
        """ initialises the insatnce """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
