#!/usr/bin/python3
""" read_file reads a file and prints to stdout """


def read_file(filename=""):
    """ opens file 'filename' into myfile and then prints the contents """
    with open(filename, encoding="utf-8") as myfile:
        read_data = myfile.read()

    print(read_data, end="")
