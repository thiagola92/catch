import unittest
from unittest import TestCase
from unittest.mock import Mock

from la_catch import catch


class CatchError(Exception):
    pass


f = Mock()
e = CatchError()


class TestCall(TestCase):
    """
    Test catch and calling a function.
    We go through every way the user can pass the arguments.
    """

    def setUp(self) -> None:
        f.reset_mock(return_value=True, side_effect=True)

        return super().setUp()
    
    def test_call_1(self):
        self._call_1()

        f.assert_called_once_with(self, e)
    
    def test_call_2(self):
        self._call_2(1)

        f.assert_called_once_with(self, 1, e)
    
    def test_call_3(self):
        self._call_3(1, 2, 3)

        f.assert_called_once_with(self, 1, 2, 3, e)
    
    def test_call_4(self):
        self._call_4(a=1)

        f.assert_called_once_with(self, e, a=1)
    
    def test_call_5(self):
        self._call_5(a=1, b=2, c=3)

        f.assert_called_once_with(self, e, a=1, b=2, c=3)
    
    def test_call_6(self):
        self._call_6(1, b=2)

        f.assert_called_once_with(self, 1, e, b=2)

    @catch(CatchError, f)
    def _call_1(self):
        raise e

    @catch(CatchError, f)
    def _call_2(self, a):
        raise e

    @catch(CatchError, f)
    def _call_3(self, a, b, c):
        raise e

    @catch(CatchError, f)
    def _call_4(self, a):
        raise e

    @catch(CatchError, f)
    def _call_5(self, a, b, c):
        raise e

    @catch(CatchError, f)
    def _call_6(self, a, b):
        raise e


if __name__ == "__main__":
    unittest.main()
