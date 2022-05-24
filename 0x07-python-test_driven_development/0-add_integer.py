#!/usr/bin/python3
"""
0-add_integer module
adds 2 numbers and returns an int
"""


def add_integer(a, b=98):
    """
    adds a to b, raises error
    if either not int or float
    """

    if a is None:
        raise TypeError("a must be an integer")

    if a == float('inf') or a == float('-inf'):
        raise OverflowError("cannot convert float infinity to integer")

    if b == float('inf') or b == float('-inf'):
        raise OverflowError("cannot convert float infinity to integer")

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    else:
        a = int(a)

    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        b = int(b)

    return a + b
