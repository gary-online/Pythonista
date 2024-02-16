import unittest
import shape_area

class TestArea(unittest.TestCase):

    def test_triangle(self):
        self.assertEqual(shape_area.triangle(10, 5), 25)

    def test_rectangle(self):
        self.assertEqual(shape_area.rectangle(6, 7), 42)

    def test_square(self):
        self.assertEqual(shape_area.square(7), 49)
        
if __name__ == '__main__':
    unittest.main()