import unittest

from ..mystery_5 import mystery_5

class TestMystery5(unittest.TestCase):
    """ """

    def test_minimal_list_input(self):
        """"""
        self.assertEqual(mystery_5([], []), [])
    def test_list_of_int_input(self):
        """"""
        self.assertEqual(mystery_5([5,6,98,2,7], []), [2, 5, 6, 7, 98])
    def test_list_of_str_input(self):
        """ if b is empty list"""
        self.assertEqual(mystery_5(['a', 'A', 'Z', 'y'], []), ['A','Z','a','y'])
    def test_list_of_str2_input(self):
        """ if b isn't empty list"""
        self.assertEqual(mystery_5(['a', 'A', 'Z', 'y'], ['z', 5]), ['z',5, 'A','Z','a','y'])
    def test_int_input(self):
        """if a is an int"""
        with self.assertRaises(AssertionError):
            mystery_5(5, [])
    def test_str_input(self):
        """if a is a str"""
        with self.assertRaises(AssertionError):
            mystery_5('a', [])
    def test_int2_input(self):
        """if b is an int"""
        with self.assertRaises(AssertionError):
            mystery_5([], 5)
    def test_str2_input(self):
        """if b is a str"""
        with self.assertRaises(AssertionError):
            mystery_5([], 'a')
    
        
