import unittest

from ..mystery_9 import mystery_9

class TestMystery9(unittest.TestCase):
    """ """

    def test_minimal_input(self):
        """"""
        self.assertEqual(mystery_9([]), [])
    def test_list_of_int_input(self):
        """"""
        self.assertEqual(mystery_9([1,2,3,4]), [1, 2, 3, 4])
    def test_list_of_int2_input(self):
        """"""
        self.assertEqual(mystery_9([6,2,8,3,15,9]), [2, 3, 6, 8, 9, 15])
    def test_list_of_str_input(self):
        """"""
        self.assertEqual(mystery_9(['om','ni','a']), ['a', 'ni', 'om'])
    def test_list_of_str2_input(self):
        """"""
        self.assertEqual(mystery_9(['om','ni','ag','om','ag']), ['ag', 'ag', 'ni', 'om', 'om'])    
    def test_string_input(self):
        """"""
        with self.assertRaises(AssertionError):
            mystery_9('omnia')
    def test_int_input(self):
        """"""
        with self.assertRaises(AssertionError):
            mystery_9(56)
