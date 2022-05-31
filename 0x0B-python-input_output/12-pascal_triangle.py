#!/usr/bin/python3
""" creates a pascals triangle """


def pascal_triangle(n):
    """ creates a pascals triangle """

    triangle = []
    if n >= 0:
        for i in range(n):
            row = [1]
            if i > 0:
                for j in range(i):
                    row.append(sum(triangle[-1][j:j+2]))
            triangle.append(row)

    return triangle
