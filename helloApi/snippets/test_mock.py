from unittest.mock import Mock,patch
import unittest
from .original import Original

@patch('snippets.original.Original')
class MyTest(unittest.TestCase):
    def test_one(self, MockSomeClass):
        self.assertIs(Original, MockSomeClass)
    def test_two(self, MockSomeClass):
        #self.assertIs(Original, MockSomeClass)
        o=Original()
        o.func1(1)
        MockSomeClass.func1.assert_called_once_with(1)
