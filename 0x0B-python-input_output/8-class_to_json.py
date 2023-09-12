#!/usr/bin/python3
""" Defines  a function that returns the
dictionary for JSON serialization of an object"""


def class_to_json(obj):
    """
    A function that returns the dictionary 
    for JSON serialization of an object.
    Args:
        obj: an instance of a Class.
    Return:
        dictionary for JSON serialization of
        an object.
    """
    return obj.__dict__
