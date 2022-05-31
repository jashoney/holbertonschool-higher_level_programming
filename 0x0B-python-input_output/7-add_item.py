#!/usr/bin/python3
""" adds args to a list then saves the list """


import json


from sys import argv
to_file = __import__("5-save_to_json_file").save_to_json_file
from_file = __import__("6-load_from_json_file").load_from_json_file
filename = "add_item.json"

try:
    mylist = from_file(filename)
except Exception:
    mylist = []

for myarg in argv[1:]:
    mylist.append(myarg)

to_file(mylist, filename)
