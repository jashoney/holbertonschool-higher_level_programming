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

    if ((type(a) is not int) and (type(a) is not float) or (a is None)):
        raise TypeError("a must be an integer")

    if isinstance(a, float):
        a = int(a)

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    if isinstance(b, float):
        b = int(b)

    return (a + b)
