#!/usr/bin/python3
""" loads JSON representation to an object """


import json


def from_json_string(my_str):
    """ converts a string from JSON repr then returns it """
    return json.loads(my_str)
