import unittest
from unittest import TestCase

from la_catch import Catch


class TestDecoratorCallbackArgs(TestCase):
    """
    Test if arguments from initilization, function and the exception
    are being pass to callback
    """

    def setUp(self) -> None:
        self._exception = Exception("Exception")

    def test_decorator_1(self):
        def test(a, b, c, d, exception):
            assert a == 1
            assert b == 2
            assert c == 3
            assert d == 4
            assert exception == self._exception

        @Catch(Exception, test, a=1, b=2)
        def func(c, d):
            raise self._exception

        func(3, 4)
        func(3, 4)

    def test_decorator_2(self):
        def test(a, b, c, d, exception):
            assert a == 1
            assert b == 2
            assert c == 3
            assert d == 4
            assert exception == self._exception

        @Catch(Exception, test, a=1, b=2)
        def func(c, d):
            raise self._exception

        func(3, d=4)
        func(3, d=4)

    def test_decorator_3(self):
        def test(a, b, c, d, exception):
            assert a == 1
            assert b == 2
            assert c == 3
            assert d == 4
            assert exception == self._exception

        @Catch(Exception, test, a=1, b=2)
        def func(c, d):
            raise self._exception

        func(c=3, d=4)
        func(c=3, d=4)


if __name__ == "__main__":
    unittest.main()
