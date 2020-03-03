from .b import B
from .a import A
from unittest.mock import Mock,patch, MagicMock
import unittest
class Foo:
    def iter(self):
        for i in [1, 2, 3]:
            yield i
    def foo1(self, a):q
        pass   

class Autospec(unittest.TestCase):
    def test_autospect(self):
        with patch.object(Foo, 'foo1', autospec=True) as mock_foo:
            mock_foo.return_value = 'foo2'
            f = Foo()
            self.assertEqual(f.foo1('b'),'foo2')
            mock_foo.assert_called_once_with(f,'b')
    def setUp(self):
        pass
    def tearDown(self):
        pass
    @classmethod
    def setUpClass(cls):
        pass
    @classmethod
    def tearDownClass(cls):
        pass

class Mock_generate_a_method(unittest.TestCase):
    def test_mock_generate_a_method(self):
        mock_foo = MagicMock()
        mock_foo.iter.return_value = iter([2, 3])
        for item in mock_foo.iter(): #list(mock_foo.iter())
            print(item)
        mock_foo.iter.assert_called_once()
class TestMockMethodOrAttribute(unittest.TestCase):
    def test_mock_method_attr(self):
        with patch.object(A,'foo') as mocked_method:  # Note A not b.A
            mocked_method.return_value='new'
            y = B()
            self.assertEqual(y.bar('a'),"new")
            mocked_method.assert_called_with('a')

class TestMockClass1(unittest.TestCase):
    def test_mock_class1(self):
        mocked_a_class = Mock()
        mocked_a_instance = mocked_a_class.return_value
        mocked_a_instance.foo.return_value = 'New foo'

        with patch('snippets.b.A', mocked_a_class):  # Note b.A not a.A
            y = B()
            y.bar('a')
            y.bar('a')
            self.assertEqual(y.bar('a'),"New foo")

@patch('snippets.b.A') # Note b.A not a.A
class TestMockClass2(unittest.TestCase):
    def test_mock_class1(self, MockSomeClass):
        mocked_a_instance = MockSomeClass.return_value
        mocked_a_instance.foo.return_value = 'New New foo'
        #self.assertIs(Original, MockSomeClass)
        b = B()
        self.assertEqual(b.bar('b'),"New New foo")
        mocked_a_instance.foo.assert_called_with('b')
