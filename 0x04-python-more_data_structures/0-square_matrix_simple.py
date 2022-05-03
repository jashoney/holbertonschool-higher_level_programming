#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    rows = len(matrix)
    columns = len(matrix[0])
    my_matrix = [0] * rows
    for x in range(rows):
        my_matrix[x] = [0] * columns
    for i in range(rows):
        for j in range(columns):
            my_matrix[i][j] = int(matrix[i][j]) * int(matrix[i][j])
    return (my_matrix)
