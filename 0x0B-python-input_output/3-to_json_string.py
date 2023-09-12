#!/usr/bin/python3
""" Defines  a function that returns the JSON
representation of an object (string).
"""


def to_json_string(my_obj):
    """
    A function that returns the JSON representation of an object (string).
    Args:
        my_obj:convert it to string representations.
    Return:
        the JSON representation of an object (string).
    """
    import json
    return (json.dumps(my_obj))
