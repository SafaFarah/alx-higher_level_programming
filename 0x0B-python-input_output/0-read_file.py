#!/usr/bin/python3
""" Defines a function that reads a text file
(UTF8) and prints it to stdout"""


def read_file(filename=""):
    """A function that reads a text file
    (UTF8) and prints it to stdout.
    Args:
    filename: a text file.
    """
    with open(filename, 'r', encoding="UTF8") as f:
        read_data = f.read()
        print(read_data, end='')
