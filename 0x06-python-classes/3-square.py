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
        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Public instance method  returns the current square area.
        Returns: The current square area.
        """
        return (self.__size * self.__size)
