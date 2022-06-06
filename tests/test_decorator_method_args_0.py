import unittest
from unittest import TestCase

from la_catch import Catch


class TestDecoratorMethodArgs(TestCase):
    """Test if the callback is receiving the exception"""

    def setUp(self) -> None:
        self._exception = Exception("Exception")
        self._type_error = TypeError("Exception")

    def func(a, b, self, exception):
        assert a == 1
        assert b == 2
        assert exception == self._exception

    @Catch(Exception, func, 1, 2)
    def test_decorator(self):
        raise self._exception

    def func2(a, self, b, exception):
        assert a == 1
        assert b == 2
        assert exception == self._exception

    @Catch(Exception, func2, 1, b=2)
    def test_decorator_2(self):
        raise self._exception

    def func3(self, a, b, exception):
        assert a == 1
        assert b == 2
        assert exception == self._exception

    @Catch(Exception, func3, a=1, b=2)
    def test_decorator_3(self):
        raise self._exception


if __name__ == "__main__":
    unittest.main()
