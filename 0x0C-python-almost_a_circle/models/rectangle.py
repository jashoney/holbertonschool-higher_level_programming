#!/usr/bin/python3
""" creates a Rectangle object from class Base """

from models.base import Base


class Rectangle(Base):
    """
        class Rectangle inherits from class Base
        has attributes width and height, optional x, y
        id attributes is set from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ instance constructor """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def update(self, *args, **kwargs):
        """ assigns new values to the attributes using *args
            if *args is NULL or empty uses **kwargs dict
        """
        if args is not None and len(args) > 0:
            for count, arg in enumerate(args):
                if count == 0:
                    self.id = arg
                elif count == 1:    
                    self.width = arg
                elif count == 2:
                    self.height = arg
                elif count == 3:
                    self.x = arg
                elif count == 4:
                    self.y = arg
        elif kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def __str__(self):
        """ overrides the __str__ method """
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}")

    def display(self):
        """ a public method that prints the instance
            using the # character in stdout
            indents spaces x wide, y newlines before printing
        """
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def area(self):
        """ defines an publicattribute area """
        return self.__width * self.__height

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, val):
        """ width setter """
        if type(val) is not int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, val):
        """ height setter """
        if type(val) is not int:
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, val):
        """ x setter """
        if type(val) is not int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        """ width getter """
        return self.__y

    @y.setter
    def y(self, val):
        """ y setter """
        if type(val) is not int:
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def to_dictionary(self):
        """ a public method that returns
            the dict of a rectangle instance
        """
        newdict = {'id': self.id,
                   'width': self.width,
                   'height': self.height,
                   'x': self.x,
                   'y': self.y}
        return newdict
