#!/usr/bin/python3
"""A class Rectangle that inherits from
BaseGeometry (7-base_geometry.py).
(task based on 8-rectangle.py)
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle"""

    def __init__(self, width, height):
        """Creates new object of Rectangle.
        Args:
            width: width of rectangle.
            height: height of rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Finds area of a rectangle.
        Return:area of a rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """ Function prints rectangle
        description:[Rectangle] <width>/<height>.
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
