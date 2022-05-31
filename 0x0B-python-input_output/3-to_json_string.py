#!/usr/bin/python3
""" returns JSON representation of an object (string) """


import json


def to_json_string(my_obj):
    """ converts a string to JSON repr then returns it """
    return json.dumps(my_obj)
