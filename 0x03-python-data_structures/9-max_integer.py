#!/usr/bin/python3

def max_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        return (None)
    test = my_list[0]
    for i in range(length):
        if my_list[i] > test:
            test = my_list[i]
    return(test)
