import unittest

class TestString(unittest.TestCase):
    
    def runTest(self):
        self.assertEqual( 'a'*4, 'aaaa')

class TestUCase(unittest.TestCase) :
    
    def runTest(self):
        self.assertEqual('gama'.upper(), 'GAMA')


if __name__ == '__main__':

    suite = unittest.TestSuite([TestString(), TestUCase()])
    unittest.TextTestRunner().run(suite)