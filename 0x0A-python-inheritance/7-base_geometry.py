#!/usr/bin/python3
"""
    class BaseGeometry definition
"""


class BaseGeometry:
    """
        defines an instance of class BaseGeometry
    """

    def area(self):
        """
             creates a area value
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            validates value as an integer
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
