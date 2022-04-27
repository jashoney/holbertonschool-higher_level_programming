#!/usr/bin/python3
def remove_char_at(str, n):
    strlen = len(str)
    if n < 0:
        return (str)

    if n < strlen:
        return (str[0:n] + str[n+1:])

    elif n == strlen:
        return (str[0:n])

    else:
        return (str)
