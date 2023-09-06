#!/usr/bin/python3
"""Class Rectangle that defines a rectangle."""


class Rectangle:
    """
    A class Rectangle that defines a Rectangle.

    Attributes:
        width: The width  of a rectangle
        width: The height  of a rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        The constructor for rectangle  class.

        Parameters:
            width: The width  of a rectangle.
            width: The height  of a rectangle.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Public instance method  returns the current rectangle width.
        Returns: The current rectangle width.
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Public instance method  sets the rectangle width..
        Paramerters:
            value: new width to set width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Public instance method  returns the current rectangle height.

        Returns: The current rectangle height.
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Public instance method  sets the rectangle height.

        Paramerters:
            value: new size to set rectangle height.
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
