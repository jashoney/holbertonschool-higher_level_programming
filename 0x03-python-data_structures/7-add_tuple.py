#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    i = len(tuple_a)
    j = len(tuple_b)
    a = int(tuple_a[0] if i >= 1 else 0) + int(tuple_b[0] if j >= 1 else 0)
    b = int(tuple_a[1] if i >= 2 else 0) + int(tuple_b[1] if j >= 2 else 0)
    return (a, b)
