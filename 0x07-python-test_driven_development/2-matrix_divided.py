#!/usr/bin/python3
"""
function matrix_divided takes a matrix and divides
each element by the variable div
"""

def matrix_divided(matrix, div):
    """ 
    divides a matrix by the number div
    element by element
    """

    if div == None:
        raise TypeError("matrix_divided() missing 1 required positional argument: 'div'")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if matrix == None:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    rows = len(matrix)
    cols = len(matrix[0])

    new_matrix = [0] * rows
    for i in range(rows):
        new_matrix[i] = [0] * cols

    for i in range(rows):
        if len(matrix[i]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    for i in range(rows):
        for j in range(cols):
            number = matrix[i][j]
            if type(number) is not int and type(number) is not float:
                raise TypeError("matrix must be a matrix (list of lists)",
                                " of integers/floats")
            new_matrix[i][j] = round(number / div, 2)

    return new_matrix
