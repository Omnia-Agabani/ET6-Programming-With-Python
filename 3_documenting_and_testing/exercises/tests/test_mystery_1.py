from typing import Self
import unittest

from ..mystery_1 import mystery_1

class TestMystery1(unittest.TestCase):
    """ """

    def test_minimal_input(self):
        """"""
        self.assertEqual(mystery_1(0, 0), 0)
    def test_2_int_input(self):
        """"""
        self.assertEqual(mystery_1(8, 9), 17)
    def test_2_str_input(self):
        """"""
        self.assertEqual(mystery_1('s', 'a'), 'sa')
    def test_2_lists_of_int_input(self):
        """"""
        self.assertEqual(mystery_1([1,5], [4,3]), [1, 5, 4, 3])
    def test_2_lists_of_str_input(self):
        """"""
        self.assertEqual(mystery_1(['1','5'], ['4','3']), ['1', '5', '4', '3'])
    def test_2_different_type_input(self):  
        """"""
        with self.assertRaises(AssertionError):
            mystery_1('s', 1)  
    