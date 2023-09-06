#!/usr/bin/python3
"""
A module  that adds 2 integers.
a and b must be integers or floats.
Returns an integer: the addition of a and b
"""


def add_integer(a, b=98):
    """
    a function that adds 2 integers.

    parameters:
        a: first integer number
        b: second integer number
    Returns:
         the addition of a and b
    """
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != int:
        raise TypeError("b must be an integer")
    return (a + b)
