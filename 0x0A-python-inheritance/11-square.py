#!/usr/bin/python3
"""
    definition of the square class
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        a square is a rectangle class
    """

    def __init__(self, size):
        """
            instantiation of a square object
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
            returns the area of a square
        """
        return self.__size ** 2

    def __str__(self):
        """
            returns a printable format for a square instance
        """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
