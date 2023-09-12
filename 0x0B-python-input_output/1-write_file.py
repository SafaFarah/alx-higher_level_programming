#!/usr/bin/python3
""" Defines a function that writes a string to
a text file (UTF8) and returns the number of
characters written"""


def write_file(filename="", text=""):
    """ a function that writes a string to
    a text file (UTF8)
    Args:
        filename: a text file.
        text: The text to be written.
    Return:
        the number of characters written
    """
    with open(filename, 'w', encoding="UTF8",) as f:
        write_data = f.write(text)
        return write_data
