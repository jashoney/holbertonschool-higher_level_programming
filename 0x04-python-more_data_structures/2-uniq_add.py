#!/usr/bin/python3

def uniq_add(my_list=[]):
    newlist = []
    total = 0
    for i in my_list:
        if newlist.count(i):
            continue
        else:
            newlist.append(i)
            total += i
    return total
