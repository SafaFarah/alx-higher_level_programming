#!/usr/bin/python3
"""Funtion add_attribute"""


def add_attribute(object, name, value):
    """Adds a new attribute to an object if it's possible.

    Args:
        object: the object.
        name: name of the attribute.
        value: value of the attribute.
    """
    if not(hasattr(object, "__dict__")):
        raise TypeError("can't add new attribute")
    setattr(object, name, value)
