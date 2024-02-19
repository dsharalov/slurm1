
from homework1 import make_matrix

def test_with_x():
    test = make_matrix(1)
    result =""" 1 2 3 4 5
 6 7 8 9 10
 11 12 13 14 15
 16 17 18 19 20
 21 22 23 24 25"""
    assert test == result

def test_with_no_arg():
    test = make_matrix(1)
    result =""" 1 2 3 4 5
 6 7 8 9 10
 11 12 13 14 15
 16 17 18 19 20
 21 22 23 24 25"""
    assert test == result



