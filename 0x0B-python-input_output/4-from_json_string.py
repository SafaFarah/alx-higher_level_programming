#!/usr/bin/python3
""" Defines a function that returns an object
(Python data structure) represented by a JSON string
"""


def from_json_string(my_str):
    """
    A function that returns an object
    (Python data structure) represented by
    a JSON string.
    Args:
        my_str:the string representations.
    Return:
        An object (Python data structure)
        represented by a JSON string
        """
    import json
    return (json.loads(my_str))
