#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    new_list = []
    length = len(my_list) - 1
    for i in range(length + 1):
        new_list.append(my_list[length - i])
    print(new_list)
