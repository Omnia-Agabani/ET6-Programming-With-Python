from typing import Self
import unittest

from ..mystery_1 import mystery_1

class TestMystery1(unittest.TestCase):
    """ """
    def test_minimal_int_input(self):
        """"""
        self.assertEqual(mystery_1(0,0), 0)
    def test_minimal_str_input(self):
        """"""
        self.assertEqual(mystery_1('',''), '')
    def test_minimal_list_input(self):
        """"""
        self.assertEqual(mystery_1([], []), [])
    def test_2_int_input(self):
        """"""
        self.assertEqual(mystery_1(2,5), 7)
    def test_2_str_input(self):
        """"""
        self.assertEqual(mystery_1('O','A'), 'OA')
    def test_2_list_input(self):
        """"""
        self.assertEqual(mystery_1(['O','M'],['F','A']), ['O', 'M', 'F','A'])
    def test_different_type_input(self):
        """"""
        with self.assertRaises(AssertionError):
            mystery_1('O',['A'])
