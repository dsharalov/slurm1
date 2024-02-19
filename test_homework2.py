
from homework2 import pyramid

def test_with_arg():
    test = pyramid(3)
    result ="""1
2 3
4 5 6
"""
    assert test == result

def test_with_no_arg():
    test = pyramid()
    result ="""1
2 3
4 5 6
7 8 9 10
"""
    assert test == result

def test_with_error_data():
    test = pyramid(4)
    result ="""1
2 3
4 5 6
7 8 9 19"""
    assert test != result

