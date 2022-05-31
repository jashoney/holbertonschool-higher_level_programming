#!/usr/bin/python3
""" simple function to write to a file """


def write_file(filename="", text=""):
    """ writes to a file and returns the count of unicode chars written """
    with open(filename, 'w', encoding="utf-8") as myfile:
        return myfile.write(text)
