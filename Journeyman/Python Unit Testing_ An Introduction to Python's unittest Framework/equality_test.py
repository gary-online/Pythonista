import unittest

class EqualityTest(unittest.TestCase):

    def test_not_equal(self):
        self.assertEqual(6, 8-2)

    def test_equal(self):
        self.assertNotEqual(7, 4*2)

if __name__ == '__main__':
    unittest.main()