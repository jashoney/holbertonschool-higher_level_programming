#!/usr/bin/python3
"""
prints a square '#'s
"""


def print_square(size):
    """
    prints a square of size with #'s
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print()
    else:
        for rows in range(size):
            for cols in range(size):
                print("#", end="")
            print()
