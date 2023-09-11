#!/usr/bin/python3
""" 
    Module contents a function inherits_from()"""


def inherits_from(obj, a_class):
    """A function ckecks if the object is an
    instance of a class that inherited,from
    the specified class.
    Args:
        obj: object to check type.
        a_class: a class that inherited from.
    Return:
        True or False..
    """
    if type(obj) ==  a_class:
        return False
    return issubclass(type(obj), a_class)
