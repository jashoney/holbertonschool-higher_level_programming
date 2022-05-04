#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    mydict = {}
    for key in a_dictionary:
        mydict[key] = a_dictionary[key] * 2
    return (mydict)
