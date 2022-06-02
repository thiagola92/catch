import unittest
from unittest import TestCase

from la_catch import Catch


class TestContextManagerCallbackArgs(TestCase):
    """Test if the arguments and exception are being pass to callback"""

    def setUp(self) -> None:
        self._exception = Exception("Exception")

    def test_context_manager(self):
        def test(a, b, c, d, e):
            assert a == 3
            assert b == 4
            assert c == 1
            assert d == 2
            assert e == self._exception

        @Catch(Exception, test, 1, 2)
        def func(a, b):
            raise self._exception

        func(3, 4)
        func(3, 4)

    def test_context_manager_2(self):
        def test(a, b, c, d, exception):
            assert a == 3
            assert b == 4
            assert c == 1
            assert d == 2
            assert exception == self._exception

        @Catch(Exception, test, 1, d=2)
        def func(a, b):
            raise self._exception

        func(3, 4)
        func(3, 4)

    def test_context_manager_3(self):
        def test(a, b, c, d, exception):
            assert a == 3
            assert b == 4
            assert c == 1
            assert d == 2
            assert exception == self._exception

        @Catch(Exception, test, c=1, d=2)
        def func(a, b):
            raise self._exception

        func(3, 4)
        func(3, 4)

    def test_context_manager_4(self):
        def test(a, b, c, d, exception):
            assert a == 3
            assert b == 4
            assert c == 1
            assert d == 2
            assert exception == self._exception

        @Catch(Exception, test, c=1, d=2)
        def func(a, b):
            raise self._exception

        func(3, b=4)
        func(3, b=4)

    def test_context_manager_5(self):
        def test(a, b, c, d, exception):
            assert a == 3
            assert b == 4
            assert c == 1
            assert d == 2
            assert exception == self._exception

        @Catch(Exception, test, c=1, d=2)
        def func(a, b):
            raise self._exception

        func(a=3, b=4)
        func(a=3, b=4)


if __name__ == "__main__":
    unittest.main()
