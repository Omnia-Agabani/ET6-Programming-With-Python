import unittest

from ..mystery_4 import mystery_4

class TestMystery4(unittest.TestCase):
    """ """

    def test_minimal_input(self):
        """"""
        self.assertEqual(mystery_4(0), [])
    def test_int_input(self):
        """"""
        self.assertEqual(mystery_4(5), [0, 1, 2, 3, 4])
    def test_large_int_input(self):
        """"""
        self.assertEqual(mystery_4(15), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
    def test_str_input(self):
        """"""
        with self.assertRaises(AssertionError):
            mystery_4('A')
    def test_list_input(self):
        """"""
        with self.assertRaises(AssertionError):
            mystery_4(['a','b'])
