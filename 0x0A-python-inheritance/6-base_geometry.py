#!/usr/bin/python3
"""Defines a class BaseGeometry"""


class BaseGeometry:
    """
    Class BaseGeometry.
    """
    def area(self):
        """
        Public instance method that raises
        an Exception with the message area()
        is not implemented.
        """
        raise Exception("area() is not implemented")
