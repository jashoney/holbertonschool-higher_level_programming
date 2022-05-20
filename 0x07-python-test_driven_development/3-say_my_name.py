#!/usr/bin/python3
"""
contains a function to print say my name {name}
"""

def say_my_name(first_name, last_name=""):
    """ 
    prints a name
    in the form "say my name {first} {last}
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    if last_name == "":
        print(f"My name is {first_name} ")
    else:
        print(f"My name is {first_name} {last_name}")
