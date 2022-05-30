#!/usr/bin/python3
"""
    class MYlist inherits its properties from class list
"""


class MyList(list):
    """
        MyList inherits attr and methods from class list
    """

    def print_sorted(self):
        """
            prints a sorted list
        """
        print(sorted(self))
