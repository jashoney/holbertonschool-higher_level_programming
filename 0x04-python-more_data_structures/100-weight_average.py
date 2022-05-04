#!/usr/bin/python3

def weight_average(my_list=[]):
    sum = 0
    divisor = 0
    for i, j in my_list:
        sum = sum + i * j
        divisor = divisor + j

    return (sum / divisor)
