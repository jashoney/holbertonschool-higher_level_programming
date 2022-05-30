#!/usr/bin/python3
"""
    checks whether obj is an instance of class a_class
"""


def is_same_class(obj, a_class):
    """
        fn returns true if obj is an instance of class a_class, or false
    """
    return a_class == type(obj)
