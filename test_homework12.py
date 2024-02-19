import unittest

from homework12 import is_valid2, is_valid

class isValidTestCase(unittest.TestCase):
    def test_is_valid(self):
         self.assertTrue(is_valid2('()'))
         self.assertTrue(is_valid2('[]'))
         self.assertTrue(is_valid2('{}'))

    def test_is_not_valid(self):
        self.assertFalse(is_valid2('('))
        self.assertFalse(is_valid2('{)'))
        self.assertFalse(is_valid2('({)}'))

    def test_by_num(self):
        self.assertTrue(is_valid('()'))
        self.assertFalse(is_valid('(0}'))

def test_is_not_valid():
        assert not (is_valid2('('))
        assert not (is_valid2('{)'))
        assert not (is_valid2('({)}'))
