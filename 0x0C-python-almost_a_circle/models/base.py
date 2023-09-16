#!/usr/bin/python3

"""
This class will be the base of all other classes in this project
"""
import json

class Base:
    """ It is to manage id attribute in all
    future classes and to avoid duplicating the same code.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Method creates anew object of class.
        Args:
            id:......
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Static method returns the JSON string
        representation of list_dictionaries.
        Args:
            list_dictionaries: a list of
            dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == "[]":
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """ Class method that writes the JSON
        string representation of list_objs to
        a file.

        Args:
            A list of instances who inherits
            of Base.
        """
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w", encoding="utf-8") as f:
            my_obj = cls.to_json_string(list_objs)
            f.write(my_obj)
