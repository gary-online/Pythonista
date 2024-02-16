import unittest

class Testing(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('beta'.upper(), 'BETA')
        
    def test_boolean(self):
        x = True
        y = False
        self.assertEqual(x, y)

    def test_isupper(self):
        self.assertTrue('BETA'.isupper())
        self.assertFalse('Beta'.isupper())
        

if __name__ == '__main__':
    unittest.main()