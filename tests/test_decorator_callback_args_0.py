import unittest
from unittest import TestCase

from la_catch import Catch


class TestDecoratorCallbackArgs(TestCase):
    """
    Test if arguments from intialization and exception
    are being pass to callback.
    """

    def setUp(self) -> None:
        self._exception = Exception("Exception")

    def test_decorator(self):
        def test(a, b, exception):
            assert a == 1
            assert b == 2
            assert exception == self._exception

        @Catch(Exception, test, a=1, b=2)
        def func():
            raise self._exception

        func()
        func()


if __name__ == "__main__":
    unittest.main()
