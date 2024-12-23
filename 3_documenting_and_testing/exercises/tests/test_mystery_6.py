import unittest

from ..mystery_6 import mystery_6

class TestMystery6(unittest.TestCase):
    """ """

    def test_minimal_input(self):
        """"""
        self.assertEqual(mystery_6(0, 0), [])
    def test_int_input(self):
        """"""
        self.assertEqual(mystery_6(5, 2), [2, 3, 4, 5, 6])
    def test_large_int_input(self):
        """"""
        self.assertEqual(mystery_6(4, 40), [40, 41, 42, 43])
    def test_str1_input(self):
        """if a is a str"""
        with self.assertRaises(AssertionError):
            mystery_6('a', 4)
    def test_str2_input(self):
        """if b is a str"""
        with self.assertRaises(AssertionError):
            mystery_6(5, 'a')
    def test_list1_input(self):
        """if a is a list"""
        with self.assertRaises(AssertionError):
            mystery_6([1,2,3], 4)
    def test_list2_input(self):
        """if b is a list"""
        with self.assertRaises(AssertionError):
            mystery_6('a', 4)
