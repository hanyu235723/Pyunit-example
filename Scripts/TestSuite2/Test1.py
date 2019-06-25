
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_1(self):
        print("in test1 method")
    def test_2(self):
        print("in test method2")
    def tearDown(self):
        pass

if(__name__=="Test1" or __name__=="__main__"):
    unittest.main()