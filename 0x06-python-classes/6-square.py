#!/usr/bin/python3
""" definition of a classs Square """


class Square:
    """ instance of a class Square """
    def __init__(self, size=0, position=(0, 0)):
        """ initialises the instance """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ getter for size """
        return self.__size

    @property
    def position(self):
        """ getter for position """
        return self.__position

    def area(self):
        """ calcs an area """
        return self.__size**2

    @size.setter
    def size(self, new_size):
        """ setter for size """
        if type(new_size) is not int:
            raise TypeError("size must be an integer")
        elif new_size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = new_size

    @position.setter
    def position(self, new_position):
        """ setter for position """
        if type(new_position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(new_position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (new_position[0] is not int) or (new_position[1] is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (new_position[0] < 0) or (new_position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = new_postition

    def my_print(self):
        """ prints a square with a space fill from position """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__position[0]):
                if self.__position[1] == 1:
                    print(" ", end="")
            for k in range(self.__size):
                print("#", end="")
            print()
