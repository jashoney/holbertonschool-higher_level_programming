#!/usr/bin/python3
"""
    looking for True if subclass
"""


def inherits_from(obj, a_class):
    """
        function returns True is a_class inherits from obj
        but is not type obj
    """
    return isinstance(obj, a_class) and a_class != type(obj)
