import unittest
from models.base import Base

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
    
    def tearDown(self):
        """Method called after calling the
        test method and the result recorded.
        """
        pass
