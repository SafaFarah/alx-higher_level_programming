#!/usr/bin/python3

"""
This class will be the base of all other classes in this project
"""
import json
import os
import csv


class Base:
    """ It is to manage id attribute in all
    future classes and to avoid duplicating the same code.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Method creates anew object of class.
        Args:
            id: The identifier of an object.
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Class method that serializes in CSV:
        Args:
            A list of instances who inherits
            of Base.
        """
        filename = "{}.csv".format(cls.__name__)
        dic_list = []
        if list_objs is None:
            pass
        else:
            with open(filename, 'w', newline="") as f:
                if cls.__name__ == "Rectangle":
                    for o in list_objs:
                        csv.writer(f).writerow([o.id,
                                               o.width, o.height, o.x, o.y])
                elif cls.__name__ == "Square":
                    for o in list_objs:
                        csv.writer(f).writerow([o.id, o.size, o.x, o.y])

    @classmethod
    def load_from_file_csv(cls):
        """Class method that deserializes in CSV
        """
        filename = cls.__name__ + ".csv"
        obj_list = []
        try:
            with open(filename, 'r') as f:
                reader = csv.reader(f)
                for L in reader:
                    if cls.__name__ == "Rectangle":
                        dic = {"id": int(L[0]), "width": int(L[1]),
                               "height": int(L[2]), "x": int(L[3]),
                               "y": int(L[4])}
                    elif cls.__name__ == "Square":
                        dic = {"id": int(L[0]), "size": int(L[1]),
                               "x": int(L[2]), "y": int(L[3])}
                    obj = cls.create(**dic)
                    obj_list.append(obj)
        except(Exception):
            pass
        return(obj_list)
