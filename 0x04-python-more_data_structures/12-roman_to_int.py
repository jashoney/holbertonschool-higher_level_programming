#!/usr/bin/python3


def roman_char(c):
    if c == 'I':
        return 1
    if c == 'V':
        return 5
    if c == 'X':
        return 10
    if c == 'L':
        return 50
    if c == 'C':
        return 100
    if c == 'D':
        return 500
    if c == 'M':
        return 1000
    return 0


def less_than_full_value(num, sub):
    if num == 5:
        return 4
    elif num == 10:
        return 9
    elif num == 50:
        return 40
    elif num == 100:
        return 90
    elif num == 500:
        return 400
    elif num == 1000:
        if sub == 10:
            return 990
        else:
            return 900
    else:
        return 0


def roman_to_int(roman_string):

    if roman_string is None:
        return 0
    if type(roman_string) != str:
        return 0

    length = len(roman_string)
    if length == 0:
        return 0

    numlist = []
    for i in range(length):
        numlist.append(roman_char(roman_string[i]))

    sum = 0
    last_digit = 0
    for i in numlist:
        if last_digit:
            if last_digit < i:
                sum = sum - last_digit
                sum = sum + less_than_full_value(i, last_digit)
            else:
                sum = sum + i
                last_digit = i
        else:
            sum = sum + i
            last_digit = i

    return (sum)
