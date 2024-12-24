import unittest

from ..mystery_7 import mystery_7

class TestMystery7(unittest.TestCase):
    """ """

    def test_minimal_input_list(self):
        """"""
        self.assertEqual(mystery_7([], []), [])

    def test_minimal_input_string(self):
        """"""
        self.assertEqual(mystery_7('', ''), [])
    def test_input_list(self):
        """"""
        self.assertEqual(mystery_7(['Omnia','Mustafa','Fawzi','Abdulgadir'], 'b'), ['Abdulgadir'])

    def test_input_string(self):
        """"""
        self.assertEqual(mystery_7('Omnia', 'a'), ['a'])
    def test_input_int(self):
        """"""
        with self.assertRaises(AssertionError):
            mystery_7(5, 1)
    