#!/usr/bin/python3

"""
This class will be the base of all other classes in this project
"""
import json
import os


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
        dic_list = []
        if list_objs is None:
            pass
        else:
            for obj in list_objs:
                dic_list.append(obj.to_dictionary())
            string = cls.to_json_string(dic_list)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(string)

    @staticmethod
    def from_json_string(json_string):
        """
        Static method returns the list of the
        JSON string representation json_strin
        Args:
        json_string is a string representing
        a list of dictionaries
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """
        Class method returns an instance with
        all attributes already set:
        Args:
            A double pointer to a dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(2, 4)
        if cls.__name__ == "Square":
            dummy = cls(2)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Class method returns a list of
        instances """
        list_obj = []
        filename = "{}.json".format(cls.__name__)
        if os.path.exists(filename) is False:
            return list_obj
        with open(filename, "r", encoding="utf-8") as f:
            str_list = f.read()
        dic_list = cls.from_json_string(str_list)
        for dic in dic_list:
            obj = cls.create(**dic)
            list_obj.append(obj)
        return list_obj
