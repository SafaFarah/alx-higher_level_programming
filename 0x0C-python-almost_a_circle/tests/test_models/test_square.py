#!/usr/bin/python3
""" Test module to test Square  model"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch
from models.square import Square


class TestSquare(unittest.TestCase):
    """ Test: Square class to test Square
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
        self.s1 = Square(10)
        self.s2 = Square(2, 0, 0, 12)
        self.s3 = Square(8, 0, 0, 12)

    def tearDown(self):
        """Method called after calling the
        test method and the result recorded.
        """
        pass

    def test_type(self):
        """ Test: Square class type """
        t = "<class 'models.square.Square'>"
        self.assertEqual(str(Square), t)

    def test_Rect_inherit(self):
        """ Test: Square is sub class of Base
        and Rectangle class"""
        self.assertTrue(issubclass(Square, Base))
        self.assertTrue(issubclass(Square, Rectangle))

    def test_attrs(self):
        """ Test: Rectangle Square attributes """
        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s2.id, 12)
        self.assertEqual(self.s1.size, 10)
        self.assertEqual(self.s2.size, 2)
        self.assertEqual(self.s2.x, 0)
        self.assertEqual(self.s3.y, 0)

    def test_Validate_attrs(self):
        """Test: for validation of  attributes
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("2")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.s2.x = {}
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(2, 3, -1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.s1.size = -10

    def str_squ(self):
        """Test: returns [Square] (<id>) <x>/<y> - <size> """
        squ_str = "[Square] (12) 0/0 - 8\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(self.s3)
            self.assertEqual(out.getvalue(), squ_str)

    def test_num_args(self):
        """ Test: number of arguments """
        with self.assertRaises(TypeError) as e:
            s5 = Square()
        x = "Square.__init__() missing 1 required positional argument: 'size'"
        self.assertEqual(str(e.exception), x)
        with self.assertRaises(TypeError) as e:
            s6 = Square(3, 2, 5, 9, 8)
        exp22 = "Square.__init__() takes from"
        exp_2 = " 2 to 5 positional arguments but 6 were given"
        exp2 = exp22 + exp_2
        self.assertEqual(str(e.exception), exp2)

    def test_area(self):
        """ Test: The area of Square"""
        self.assertEqual(self.s1.area(), 100)
        self.assertEqual(self.s3.area(), 64)

    def test_doc(self):
        """ Test: docstring is present """
        self.assertIsNotNone(Square.__doc__)

    def test_isinstance(self):
        """ Test: Square is instance of Base  and Rectangle"""
        self.assertEqual(True, isinstance(self.s1, Base))
        self.assertEqual(True, isinstance(self.s1, Rectangle))

    def test_display(self):
        """ Test: display() taking care of x
        an y"""
        s7 = Square(2, 2, 0)
        squ = "  ##\n  ##\n"
        with patch('sys.stdout', new=StringIO()) as out:
            s7.display()
            self.assertEqual(out.getvalue(), squ)

    def test_to_dictionary(self):
        """ Test: method returns the dictionary representation of a Square"""
        dic = {'id': 12, 'x': 0, 'size': 8, 'y': 0}
        self.assertEqual(self.s3.to_dictionary(), dic)
        self.assertEqual(type(dic), dict)

    def update(self, *args, **kwargs):
        """Test: assigns a key/value argument to attributes"""
        s8 = Rectangle(10, 10, 10)
        s8.update(x=1, size=2, y=3)
        self.assertEqual(s8.x, 1)
        self.assertEqual(s8.y, 3)
        self.assertEqual(s8.size, 4)
