import unittest




from ..mystery_2 import mystery_2

class TestMystery2(unittest.TestCase):
    """ """
 def test_minimal_list_input(self):
        """"""
        self.assertEqual(mystery_2([]), None)

    def test_minimal_string_input(self):
        """"""
        self.assertEqual(mystery_2(''), None)
    def test_short_string_input(self):
        """"""
        self.assertEqual(mystery_2('Omnia Agabani'), 13)
    def test_list_of_str_input(self):
        """"""
        self.assertEqual(mystery_2(['Omnia', 'Mustafa','Fawzi','Abdulgadir']), 4)
    def test_list_of_int_input(self):
        """"""
        self.assertEqual(mystery_2([3,3,19,99]), 4)
    def test_2_different_type_input(self):  
        """"""
        with self.assertRaises(AssertionError):
            mystery_2(1)
