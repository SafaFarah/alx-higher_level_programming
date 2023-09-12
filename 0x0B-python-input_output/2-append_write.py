#!/usr/bin/python3
""" Defines a function that appends a string
at the end of a text file (UTF8) and returns
the number of characters added."""


def append_write(filename="", text=""):
    """ a function that appends a string at
    the end of a text file (UTF8)
    Args:
        filename: a text file.
        text: The text to be added.
    Return:
        the number of characters added.
    """
    with open(filename, 'a', encoding="UTF8",) as f:
        append_data = f.write(text)
        return append_data
