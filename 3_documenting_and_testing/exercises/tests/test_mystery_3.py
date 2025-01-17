import unittest

from ..mystery_3 import mystery_3

class TestMystery3(unittest.TestCase):
    """ """

    def test_minimal_input(self):
        """"""
        self.assertEqual(mystery_3(0, 0), 0)

        
    def test_2_int_input(self):
        """"""
        self.assertEqual(mystery_3(17, 23), 17)
        
    def test_2_same_int_input(self):
        """"""
        self.assertEqual(mystery_3(17, 17), 34)
    
    def test_2_str_input(self):
        """"""
        self.assertEqual(mystery_3('Omnia', 'Agabani'), 'Agabani')
        
    def test_2_same_str_input(self):
        """"""
        self.assertEqual(mystery_3('Omnia', 'Omnia'), 'OmniaOmnia')
    
    def test_2_list_same_size_input(self):
        """"""
        self.assertEqual(mystery_3([3,5], [6,2]), [3,5])
        
    def test_2_list_different_size_input(self):
        """"""
        self.assertEqual(mystery_3([3,5], [6,2,5]), [3,5])
    def test_2_list_same_list_input(self):
        """"""
        self.assertEqual(mystery_3([3,5], [3,5]), [3,5,3,5])
    def test_different_type_input(self):
        """"""
        with self.assertRaises(AssertionError):
            mystery_3('O',['A'])