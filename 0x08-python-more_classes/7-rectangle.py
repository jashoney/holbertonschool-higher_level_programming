#!/usr/bin/python3
""" class Rectangle """


class Rectangle:
    """ class Rectangle
        instance count is number_of_instances
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ instantiation """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ calculation of the area of the Rectangle object """
        return self.__width * self.__height

    def perimeter(self):
        """ calculation of the perimeter of the Rectangle object """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """ prints the rectangle, represented by hashes
            in the correct dimensions """
        my_str = ""
        if self.__width == 0 or self.__height == 0:
            return my_str
        for i in range(self.__height):
            for j in range(self.__width):
                print(self.print_symbol, end="")
            if i < self.__height - 1:
                print()
        return my_str

    def __repr__(self):
        """ recreates a rectangle
            into a string
            in the correct dimensions """
        my_str = ""
        if self.__width == 0 or self.__height == 0:
            return my_str
        my_str = "Rectangle(" + str(self.__width)
        my_str = my_str + ", " + str(self.__height) + ")"
        return my_str

    def __del__(self):
        """ removes an instance """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
