#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    new_list = []
    length = len(my_list)
    for i in range(length):
        new_list.append(my_list[length - 1 - i])
    for i in range(length):
        print(new_list[i])
