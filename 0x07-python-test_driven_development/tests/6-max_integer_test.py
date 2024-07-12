import unittest
from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):

    def test_positive_integers(self):
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)

    def test_negative_integers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()
