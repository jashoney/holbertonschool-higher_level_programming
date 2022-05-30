#!/usr/bin/python3
"""
    class BaseGeometry definition
"""


class BaseGeometry:
    """
        defines an instance of class BaseGeometry
    """
    def __init__(self):
        """
            instantiates
        """
        pass

    def area(self):
        """
            defines an area property
        """
        raise Exception("area() is not implemented")
