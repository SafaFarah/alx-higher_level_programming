#!/usr/bin/python3
"""
The divide module.
contents a function that divides all elements of a matrix.
matrix must be a list of lists of integers
"""


def matrix_divided(matrix, div):
    """
    a function that divides all elements of a matrix.
    parameters:
        matrix: a list of lists of integers or floats.
        div: a number (integer or float)
    Returns: a new matrix
    """
    divmatrix = []

    if type(div) != int and type(div) != float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if div is None:
        raise TypeError('div must be a number')
    Error = 'matrix must be a matrix(list of lists) of integers/floats'
    if matrix == [] or matrix is None:
        raise TypeError(Error)
    if type(matrix) != list:
        raise TypeError(Error)
    for row in matrix:
        if type(row) != list:
            raise TypeError(Error)
    length = len(matrix[0])
    for row in matrix:
        divrow = []
        if length != len(row):
            raise TypeError('Each row of the matrix must have the same size')
        for num in row:
            if type(num) != int and type(num) != float:
                raise TypeError(Erorr)
            divrow.append(round(num / div, 2))
        divmatrix.append(divrow)
    return divmatrix
