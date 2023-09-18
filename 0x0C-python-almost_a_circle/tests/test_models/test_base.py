#!/usr/bin/python3
""" Test module to test Base model"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json


class TestBase(unittest.TestCase):
    """
    Test: Square class to test Base model
    """

    @classmethod
    def setUpClass(cls):
        """A class method called before tests
        in an individual class run. """
        pass

    @classmethod
    def tearDownClass(cls):
        """ A class method called after tests
        in an individual class have run."""
        pass

    def setUp(self):
        """Method called to prepare the test
        fixture. """
        Base._Base__nb_objects = 0
        self.b1 = Base()
        self.b2 = Base(12)
        self.b3 = Base()

    def tearDown(self):
        """Method called after calling the
        test method and the result recorded.
        """
        pass

    def test_type(self):
        """ Test: Base class type """
        t = "<class 'models.base.Base'>"
        self.assertEqual(str(Base), t)

    def test_attrs(self):
        """ Test: Base class  attributes """
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 12)
        self.assertEqual(self.b3.id, 2)

    def test_doc(self):
        """ Test: docstring is present """
        self.assertIsNotNone(Rectangle.__doc__)

    def test_args_num(self):
        """ Test: number of arguments. """
        with self.assertRaises(TypeError) as e:
            Base.__init__()
        s = "Base.__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)
        with self.assertRaises(TypeError) as e:
            b4 = Base(1, 2)
        s1 = "Base.__init__() takes from 1 to 2"
        s2 = " positional arguments but 3 were given"
        s3 = s1 + s2
        self.assertEqual(str(e.exception), s3)

    def test_to_json_string(self):
        """ Test: returns the JSON string
        representation of list_dictionaries"""
        s1 = Square(10, 7, 2, 8)
        dic = s1.to_dictionary()
        json_dic = [{"x": 7, "size": 10, "id": 8, "y": 2}]
        json_str = Base.to_json_string([dic])
        self.assertNotEqual(dic, json_dic)
        self.assertEqual(type(dic), dict)
        self.assertEqual(type(json_str), str)
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_from_json_str(self):
        """ Test: returns the list of the JSON string representation."""
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string(None), [])
        L_input = [{'x': 7, 'size': 10, 'id': 8, 'y': 2}]
        json_L_input = Square.to_json_string(L_input)
        L_output = Square.from_json_string(json_L_input)
        out = [{'x': 7, 'size': 10, 'id': 8, 'y': 2}]
        self.assertEqual(L_output, out)
        self.assertTrue(type(L_output), list)

    def test_save_to_file(self):
        """ Test: method writes the JSON
        string representation of list_objs to a file"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        r1 = Rectangle(10, 7, 2, 8, 12)
        Rectangle.save_to_file([r1])
        r = [{"y": 8, "x": 2, "id": 12, "width": 10, "height": 7}]
        with open("Rectangle.json", "r") as f:
            self.assertNotEqual(f.read(), r)

    def test_load_from_file(self):
        """Test: method returns a list of instances: """
        s1 = Square(10, 2, 8)
        s2 = Square(2, 4)
        _list = [s1, s2]
        Square.save_to_file(_list)
        list_out = Square.load_from_file()
        self.assertNotEqual(id(_list[0]), id(list_out[0]))
        self.assertEqual(str(_list[0]), str(list_out[0]))

    def test_create(self):
        """ Test: method returns an instance with attributes already set. """
        r1 = Rectangle(3, 5, 1)
        r1_dic = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dic)
        self.assertEqual(str(r1), str(r2))
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)
