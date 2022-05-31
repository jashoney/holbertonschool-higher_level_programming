#!/usr/bin/python3
""" creates an object by reading a JSON file """


import json


def load_from_json_file(filename):
    """ converts a JSON file into an object and returns it"""
    with open(filename, 'r', encoding='utf-8') as myfile:
        return json.load(myfile)
