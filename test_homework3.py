
from homework3 import pyramid

def test_with_arg():
    test = pyramid(4)
    result ="""10\n9 8\n7 6 5\n4 3 2 1\n"""
    assert test == result

def test_with_no_arg():
    test = pyramid()
    result ="""10\n9 8\n7 6 5\n4 3 2 1\n"""
    assert test == result

def test_with_error_data():
    test = pyramid(4)
    result ="""1
2 3
4 5 6
7 8 9 19"""
    assert test != result

