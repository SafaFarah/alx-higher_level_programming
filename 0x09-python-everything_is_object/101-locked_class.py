#!/usr/bin/python3
"""A class LockedClass with no class or object attribute. """


class LockedClass:
    """
    Prevents the user from dynamically creating new instance attributes.
    Except first_name attribute.
    Attribute:
        first_name: first name attribute.
    """

    __slots__ = ["first_name"]

    def __init__(self):
        """Creates new instances of class."""

        self.first_name = "first_name"
