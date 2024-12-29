import unittest
from .draw_a_triangle import draw_a_triangle

class TestAsciiCode(unittest.TestCase):
  def test_min_int(self):
    self.assertEqual (draw_a_triangle(0),'')
  def test_int(self):
    self.assertEqual (draw_a_triangle(10),'**********\n*********\n********\n*******\n******\n*****\n****\n***\n**\n*\n')
  
