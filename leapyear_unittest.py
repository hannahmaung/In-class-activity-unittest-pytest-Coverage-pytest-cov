#Unit test for leap year program 


import unittest 
import leapyear

class testCase(unittest.TestCase):

    def setup(self):
        self.leapyear = leapyear()
    #Test 1 will pass 
    def test1(self):
        self.assertEqual(leapyear.check("2018"),(False))
    #Test 2 will pass
    def test2(self):
        self.assertEqual(leapyear.check("2024"), (True))
    #Test 3 will pass
    def test3(self):
        self.assertEqual(leapyear.check("2012"),(True))

if __name__ == "__main__":
    unittest.main()