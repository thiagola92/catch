import unittest
from unittest import TestCase
from unittest.mock import Mock

from la_catch import catch


class CatchError(Exception):
    pass


f = Mock()
e = CatchError()


class TestIncludeArgs(TestCase):
    """
    Test excluding arguments from functions.

    While this test have "include_args" in the name,
    this is just because the argument in the function is called so.

    How the default behavior is including arguments,
    we don't need to test it (it's already tested in others tests).
    However we have to test if it's excluding as expected.
    """

    def setUp(self) -> None:
        f.reset_mock(return_value=True, side_effect=True)

        return super().setUp()
    
    def test_call_1(self):
        TestIncludeArgs._call_1()

        f.assert_called_once_with(e)
    
    def test_call_2(self):
        self._call_2()

        f.assert_called_once_with(e)
    
    def test_call_3(self):
        self._call_3(1)

        f.assert_called_once_with(e)
    
    def test_call_4(self):
        self._call_4(a=1)

        f.assert_called_once_with(e)
    
    def test_call_5(self):
        self._call_5()

        f.assert_called_once_with(e)
    
    def test_call_6(self):
        self._call_6(1)

        f.assert_called_once_with(e)
    
    def test_call_7(self):
        self._call_7(1, 1)

        f.assert_called_once_with(e)
    
    def test_call_8(self):
        self._call_8(1, b=1)

        f.assert_called_once_with(e)

    @catch(CatchError, f, include_args=False)
    def _call_1():
        raise e

    @catch(CatchError, f, include_args=False)
    def _call_2(self):
        raise e

    @catch(CatchError, f, include_args=False)
    def _call_3(self, a):
        raise e

    @catch(CatchError, f, include_args=False)
    def _call_4(self, a):
        raise e

    @catch(CatchError, f, include_args=False)
    def _call_5(self, a=1):
        raise e

    @catch(CatchError, f, include_args=False)
    def _call_6(self, a, b=1):
        raise e

    @catch(CatchError, f, include_args=False)
    def _call_7(self, a, b=1):
        raise e

    @catch(CatchError, f, include_args=False)
    def _call_8(self, a, b=1):
        raise e


if __name__ == "__main__":
    unittest.main()
