#!/usr/bin/python3
"""Defines a class Student defines a student """


class Student:
    """
    A class Student that defines a student by:
    Public instance attributes:
        first_name - last_name - age.
    """

    def __init__(self, first_name, last_name, age):
        """Creates new object of Student.
        Args:
            first_name: first name of student.
            last_name: last name of student.
            age: age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation
        of a Student instance.
        Return:
             the dictionary description
        """
        if attrs is None:
            return self.__dict__

        _dict = {}
        for i in attrs:
            try:
                _dict[i] = self.__dict__[i]
            except Exception:
                pass
        return _dict
