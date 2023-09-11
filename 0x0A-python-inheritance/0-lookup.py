#!/usr/bin/python3
""" module returns the list of available attributes and methods of an object
"""


def lookup(obj):

    """
    a function returns the list of attributes and methods of an object.

    Arg:
        object of class
    Return:
        list of available attributes and methods of an object.

    """
    return dir(obj)
