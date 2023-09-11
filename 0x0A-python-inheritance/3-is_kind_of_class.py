#!/usr/bin/python3
"""
    module contents function that checks
    object of class
"""


def is_kind_of_class(obj, a_class):
    """
    a function checks  if the object is an
    instance of specified class, or if the
    object is an instance of a class that
    inherited from.
    arg:
        obj: the object.
        a_class: the class.
    Return:
        True or False.
    """
    return (isinstance(obj, a_class))
