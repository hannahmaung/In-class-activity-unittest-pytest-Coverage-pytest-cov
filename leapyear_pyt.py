#Pytest for Leap Year program

import pytest
import leapyear

#This test should pass
def test_1():
    input = "2018"
    assert leapyear.check(input) == False

#This pass should pass 
def test_2():
    input = "2024"
    assert leapyear.check(input) == True

#This pass should pass
def test_3():
    input = "2012"
    assert leapyear.check(input) == True  

if __name__ == "__main__":
    pytest.main()

