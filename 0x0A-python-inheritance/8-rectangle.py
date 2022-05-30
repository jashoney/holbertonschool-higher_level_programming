#!/usr/bin/python3
"""
    defines a class Rectangle a sub of basegeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        class Rectangle inherits from class BaseGeomtry
    """

    def __init__(self, width, height):
        """
            instance creator for class Rectangle
            width and height are private
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
