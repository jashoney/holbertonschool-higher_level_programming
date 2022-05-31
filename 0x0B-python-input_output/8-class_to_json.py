#!/usr/bin/python3
""" has a fn that returns a dict desc with simple data structure """


def class_to_json(obj):
    """ returns a dict description with simple data structure """
    return obj.__dict__
