#!/usr/bin/python3
"""Class Square that defines a square."""


class Square:
    """
    An empty class Square that defines a square.

    Attributes:
        size(int): The size of a square.
        position(int, int): A tuple of 2 positive integers.
        """

    def __init__(self, size=0, position=(0, 0)):
        """
        The constructor for Square class.

        Parameters:
            size(int): The size of a square.
            position(int, int): A tuple of 2 positive integers.
        """
        self.__size = size
        self.__position = position

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

    def my_print(self):

        """Print the square with the # character."""

        if self.__position[1] > 0:
            for x in range(self.__position[1]):
                print()
        for i in range(self.__size):
            for p in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print()

    @property
    def position(self):
        """
        Public instance method  returns  current square positon.

        Returns: The current square position..
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        Public instance method  sets the square position.

        Paramerters:
            value: new postion.
        """
        if (type(n) != int for n in value) or (type(value) != tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if(len(value) != 2) or (num < 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
