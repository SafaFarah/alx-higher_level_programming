#!/usr/bin/python3
"""Class Square that defines a square."""


class Square:
    """
    An empty class Square that defines a square.

    Attributes:
        size: The size of a square.
    """
    def __init__(self, size=0):
        """
        The constructor for Square class.

        Parameters:
            size(int): The size of a square.
        """
        self.__size = size

    @property
    def size(self):
        """
        Public instance method  returns the current square size.
        Returns: The current square size.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Public instance method  sets the square size.
        Paramerters:
            value: new size to set size
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Public instance method  returns the current square area.
        Returns: The current square area.
        """
        return (self.__size * self.__size)
