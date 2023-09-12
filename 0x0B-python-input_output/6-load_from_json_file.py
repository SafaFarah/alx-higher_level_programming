#!/usr/bin/python3
"""
Defines  a function that creates an Object
from a JSON file.
"""


def load_from_json_file(filename):
    """
    a function that creates an Object
    from a JSON file.
    Args:
        filename: a JSON file.
    """
    import json
    with open(filename, "r", encoding="utf-8") as f:
        return (json.load(f))
