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
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Public instance method  returns the current square area.
        Returns: The current square area.
        """
        return (self.__size * self.__size)
