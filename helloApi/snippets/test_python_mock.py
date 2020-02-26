import unittest
from django.test import TestCase
from unittest.mock import Mock,patch
from .calling import CallingClass
from .original import Original
class Test_python_mock(TestCase):
    mock = Mock(test='bb')
    @patch.object(CallingClass,'test', mock.test)
    def test_mock_attr(self):
        self.assertEqual(CallingClass.test,'bb')

    def test_mock_method(self):
        mock = Mock(return_value='300')
        CallingClass.func = mock
        self.assertEqual(CallingClass.func(),'300')

    def test_mock_instance_method(self):
        mock = Mock(return_value='300')
        c = CallingClass()
        c.func2 = mock
        self.assertEqual(c.func3(),'300a')

    def test_mock_instance_method4(self):
        with patch.object(Original, 'foo', autospec=True) as mock_foo:
            mock_foo.return_value = 'foo2'
            c = CallingClass()
            self.assertEqual(c.func4(),'foo2')
