#!/usr/bin/python3
"""Class Rectangle that defines a rectangle."""


class Rectangle:
    """
    A class Rectangle that defines a Rectangle.

    Attributes:
        width: The width  of a rectangle
        width: The height  of a rectangle.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        The constructor for rectangle  class.

        Parameters:
            width: The width  of a rectangle.
            width: The height  of a rectangle.
        """
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

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

    def area(self):
        """
        Public instance method  returns the current rectangle  area.
        Returns: The current rectangle area.
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Public instance method  returns the current rectangle  perimeter.
        Returns: The current rectangle  perimeter.
        """
        if (self.__width == 0 or self.__height == 0):
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Print the rectangle  with the # character."""
        rectangle = []

        if self.__width == 0 or self.__height == 0:
            return ""

        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append(str(self.print_symbol))
            rectangle.append("\n")
        rectangle.pop()
        return "".join(rectangle)

    def __repr__(self):
        """
        return a string representation of the rectangle,
        to be able to recreate a new instance by using eval function
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes an instance of a class
        """
        print("{:s}".format("Bye rectangle..."))
        type(self).number_of_instances -= 1
