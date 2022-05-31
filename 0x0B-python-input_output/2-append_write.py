#!/usr/bin/python3
""" simple function to write by appending to a file """


def append_write(filename="", text=""):
    """appends to a file and returns the count of unicode chars written """
    with open(filename, 'a', encoding="utf-8") as myfile:
        return myfile.write(text)
