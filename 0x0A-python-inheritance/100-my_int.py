#!/usr/bin/python3
"""
Module contents a class MyInt that inherits from int
"""


class MyInt(int):
    """A  class MyInt that inherits from int.
    has == and != operators inverted
    Args:
        number: integer number.
    """
    def __init__(self, number):
        """Creates new object of class MyInt.
        Args:
            number: integer number.
        """
        self.__number = number

    def __eq__(self, other):
        """Method to define the equality logic
        for comparing two objects using the
        equal operator
        """
        return self.__number != other

    def __ne__(self, other):
        """Method to define the inequality
        logic for comparing two objects using
        the not equal operator.
        """
        return self.__number == other
