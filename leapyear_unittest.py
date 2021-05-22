#Unit test for leap year program 


import unittest 
import leapyear

class testCase(unittest.TestCase):

    def setup(self):
        self.leapyear = leapyear()
    #Test 1 is going to fail because 2018 is not a leap year but it is set to True
    def test1(self):
        self.assertEqual(leapyear.check("2018"),(False))
    #Test 2 is going to pass
    def test2(self):
        self.assertEqual(leapyear.check("2024"), (True))
    #Test 3 is going to pass 
    def test3(self):
        self.assertEqual(leapyear.check("2012"),(True))

if __name__ == "__main__":
    unittest.main()