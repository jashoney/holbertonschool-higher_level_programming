#!/usr/bin/python3
""" writes an object to a text file using JSON repr """


import json


def save_to_json_file(my_obj, filename):
    """ converts a string from JSON repr then saves it to filename """
    with open(filename, 'w', encoding='utf-8') as myfile:
        myfile.write(json.dumps(my_obj))
