import unittest

from ..mystery_8 import mystery_8

class TestMystery8(unittest.TestCase):
    """ """

    def test_minimal_input(self):
        """"""
        self.assertEqual(mystery_8([], ''), [])
    def test_minimal_string_input(self):
        """"""
        self.assertEqual(mystery_8('', ''), [])
    def test_list2_input(self):
        """a is a list of str"""
        self.assertEqual(mystery_8(['a', 'g', 'a', 'b', 'a', 'n', 'i'], 'a'), ['a','a','a'])
    def test_string_input(self):
        """"""
        self.assertEqual(mystery_8('omnia agabani', 'a'), ['a','a','a','a'])
    def test_list3_input(self):
        """a and b are lists"""
        with self.assertRaises(AssertionError):
            mystery_8(['o', 'm', 'n', 'i', 'a'], ['a','g','a','b','a','n', 'i'])
    def test_list4_input(self):
        """ b is a list"""
        with self.assertRaises(AssertionError):
            mystery_8('o', ['a','g','a','b','a','n', 'i'])  
    def test_int_input(self):
        """"""
        with self.assertRaises(AssertionError):
            mystery_8(0, 0)
