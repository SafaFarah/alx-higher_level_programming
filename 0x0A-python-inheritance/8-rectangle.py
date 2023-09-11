#!/usr/bin/python3
"""A class Rectangle that inherits from
BaseGeometry (7-base_geometry.py).
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle"""

    def __init__(self, width, height):
        """Creates new instances of object of
        Rectangle class.
        Args:
            width: width of rectangle.
            height: height of rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
