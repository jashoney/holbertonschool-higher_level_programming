#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Function finds and returns the largest integer in a list, 
       none if empty
    """
    if len(list) == 0:
        return None
    largest = list[0]
    i = 1
    while i < len(list):
        if list[i] > largest:
            largest = list[i]
        i += 1
    return largest
