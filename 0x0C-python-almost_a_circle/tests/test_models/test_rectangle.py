#!/usr/bin/python3
""" Test module to test Rectangle model"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch


class TestRectangle(unittest.TestCase):
    """ TestRectangle class to test Rectangle
    model"""

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
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(10, 2, 0, 0, 12)
        self.r3 = Rectangle(8, 7, 0, 0, 12)

    def tearDown(self):
        """Method called after calling the
        test method and the result recorded.
        """
        pass

    def test_Rect_inherit(self):
        """ Test: Rectangle is sub class of
        Base """
        self.assertTrue(issubclass(Rectangle, Base))

    def test_type(self):
        """ Test: Rectangle class type """
        t = "<class 'models.rectangle.Rectangle'>"
        self.assertEqual(str(Rectangle), t)

    def test_attrs(self):
        """ Test: Rectangle class  attributes """
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 12)
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r2.height, 2)
        self.assertEqual(self.r2.x, 0)
        self.assertEqual(self.r3.y, 0)

    def test_Validate_attrs(self):
        """Test: for validation of  attributes
        """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.r2.x = {}
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 3, -1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.r1.width = -10

    def str_rect(self):
        """Test: returns [Rectangle] (<id>)
        <x>/<y> - <width>/<height>
        """
        rect_str = "[Rectangle] (12) 0/0 - 8/7\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(self.r3)
            self.assertEqual(out.getvalue(), rect_str)

    def test_num_args(self):
        """ Test: number of arguments """
        with self.assertRaises(TypeError) as e:
            r5 = Rectangle()
        exp_1 = "Rectangle.__init__() missing 2 required positional arguments:"
        exp11 = " 'width' and 'height'"
        exp1 = exp_1 + exp11
        self.assertEqual(str(e.exception), exp1)
        with self.assertRaises(TypeError) as e:
            r9 = Rectangle(2)
        exp22 = "Rectangle.__init__() missing 1"
        exp_2 = " required positional argument: 'height'"
        exp2 = exp22 + exp_2
        self.assertEqual(str(e.exception), exp2)
        with self.assertRaises(TypeError) as e:
            r6 = Rectangle(1, 3, 2, 5, 9, 8)
        exp33 = "Rectangle.__init__() takes from 3 to 6"
        exp_3 = " positional arguments but 7 were given"
        exp3 = exp33 + exp_3
        self.assertEqual(str(e.exception), exp3)

    def test_area(self):
        """ Test: The area of Rectangle"""
        self.assertEqual(self.r1.area(), 20)
        self.assertEqual(self.r3.area(), 56)

    def test_doc(self):
        """ Test: docstring is present """
        self.assertIsNotNone(Rectangle.__doc__)

    def test_isinstance(self):
        """ Test: Rectangle is instance of Base """
        self.assertEqual(True, isinstance(self.r1, Base))

    def test_display(self):
        """ Test: display() taking care of x
        an y"""
        r7 = Rectangle(2, 3, 2, 2)
        rect = "\n\n  ##\n  ##\n  ##\n"
        with patch('sys.stdout', new=StringIO()) as out:
            r7.display()
            self.assertEqual(out.getvalue(), rect)

    def test_to_dictionary(self):
        """ Test:Method returns the dictionary representation of a Rectangle"""
        dic = {'x': 0, 'y': 0, 'id': 12, 'height': 7, 'width': 8}
        self.assertEqual(self.r3.to_dictionary(), dic)
        self.assertEqual(type(dic), dict)

    def update(self, *args, **kwargs):
        """Test: assigns a key/value argument to attributes"""
        r8 = Rectangle(10, 10, 10, 10)
        r8.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r8.x, 1)
        self.assertEqual(r8.y, 3)
        self.assertEqual(r8.width, 4)
        self.assertEqual(r8.height, 2)
