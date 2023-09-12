#!/usr/bin/python3
"""
Defines a function that writes an Object to
a text file, using a JSON representation.
"""


def save_to_json_file(my_obj, filename):
    """
    a function that writes an Object to a
    text file, using a JSON representation.
    Args:
        my_obj: the object to be written to
        text file.
        filename: Text file to write to
    """
    import json
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
