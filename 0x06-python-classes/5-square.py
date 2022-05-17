#!/usr/bin/python3
""" definaition of a class Square """


class Square:
    """ class Square instance """
    def __init__(self, size=0):
        """ initialise the instance """
        self.__size = size

    @property
    def size(self):
        """ getter of size """
        return self.__size

    def area(self):
        """ calcs the area of a square """
        return self.__size**2

    @size.setter
    def size(self, new_size=0):
        """ setter of size """
        if type(new_size) is not int:
            raise TypeError("size must be an integer")
        elif new_size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = new_size

    def my_print(self):
        """ prints a square """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
