import unittest
import rectangle_perimeter

class TestArea(unittest.TestCase):

	def test_perimeter(self):
		self.assertEqual(rectangle_perimeter.get_perimeter(10, 5), 30)

	def test_error(self):
		with self.assertRaises(ValueError):
			rectangle_perimeter.get_perimeter(10, 0)
        
if __name__ == '__main__':
    unittest.main()