#!/usr/bin/python3
"""A class Square that inherits from Rectangle
(9-rectangle.py). (task based on 10-square.py)
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class Square inherits from Rectangle
    class..
    Args:
        Rectangle (Rectangle): rectangle
    """

    def __init__(self, size):
        """Creates new object of class Square.
        Args:
            size: The size of squre side
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return the square description:
        [Square] <width>/<height>
        """
        return ("[Square] {}/{}".format(self.__size, self.__size))

    def area(self):
        """Finds  the area of a square.
        Returns: the area of the square.
        """
        return self.__size * self.__size
