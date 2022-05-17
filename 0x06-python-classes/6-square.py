#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    def area(self):
        return self.__size**2

    @size.setter
    def size(self, new_size):
        if type(new_size) is not int:
            raise TypeError("size must be an integer")
        elif new_size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = new_size

    @position.setter
    def position(self, new_position):
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
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__position[0]):
                if self.__position[1] == 0:
                    print(" ", end="")
            for k in range(self.__size):
                print("#", end="")
            print()
