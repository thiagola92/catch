import unittest
from unittest import TestCase
from unittest.mock import Mock

from catch import catch


class CatchError(Exception):
    pass


function = Mock()
error = CatchError()


class TestCall(TestCase):
    def setUp(self) -> None:
        function.reset_mock(return_value=True, side_effect=True)

        return super().setUp()
    
    def test_call_1(self):
        self._call_1()

        function.assert_called_once_with(error, self)
    
    def test_call_2(self):
        self._call_2(1)

        function.assert_called_once_with(error, self, 1)
    
    def test_call_3(self):
        self._call_3(1, 2, 3)

        function.assert_called_once_with(error, self, 1, 2, 3)
    
    def test_call_4(self):
        self._call_4(a=1)

        function.assert_called_once_with(error, self, a=1)
    
    def test_call_5(self):
        self._call_5(a=1, b=2, c=3)

        function.assert_called_once_with(error, self, a=1, b=2, c=3)
    
    def test_call_6(self):
        self._call_6(1, b=2)

        function.assert_called_once_with(error, self, 1, b=2)

    @catch(CatchError, function)
    def _call_1(self):
        raise error

    @catch(CatchError, function)
    def _call_2(self, a):
        raise error

    @catch(CatchError, function)
    def _call_3(self, a, b, c):
        raise error

    @catch(CatchError, function)
    def _call_4(self, a):
        raise error

    @catch(CatchError, function)
    def _call_5(self, a, b, c):
        raise error

    @catch(CatchError, function)
    def _call_6(self, a, b):
        raise error


if __name__ == "__main__":
    unittest.main()
