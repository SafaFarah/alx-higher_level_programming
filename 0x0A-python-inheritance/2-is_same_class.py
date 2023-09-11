#!/usr/bin/python3

"""
module contents function that check object of class.
"""


def is_same_class(obj, a_class):
    """
    a function that returns True if the object
    is exactly an instance of the specified class ;otherwise False.
    arg:
        obj: the object.
        a_class: the class.
    Return:
        True or False.
    """
    if type(obj) == a_class:
        return True
    else:
        return False
