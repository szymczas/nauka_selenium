import pytest

def test_method2():
    x = 5
    y = 2
    assert  x+y== 5,"Assertion failed, Expected 7 but was " + str(x+y)
    assert  x+y== 7,"Assertion failed, Expected 2"