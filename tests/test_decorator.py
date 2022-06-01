import unittest
from unittest import TestCase
from unittest.mock import Mock

from la_catch import Catch


class CatchError(Exception):
    pass


f = Mock()
e = CatchError()


class TestCall(TestCase):
    """
    Test catching and calling a function.
    We go through every way the user can pass the arguments.
    """

    def setUp(self) -> None:
        f.reset_mock(return_value=True, side_effect=True)

        return super().setUp()

    def test_call_1(self):
        self._call_1()

        f.assert_called_once_with(self, exception=e)

    def test_call_2(self):
        self._call_2(1)

        f.assert_called_once_with(self, 1, exception=e)

    def test_call_3(self):
        self._call_3(1, 2, 3)

        f.assert_called_once_with(self, 1, 2, 3, exception=e)

    def test_call_4(self):
        self._call_4(a=1)

        f.assert_called_once_with(self, a=1, exception=e)

    def test_call_5(self):
        self._call_5(a=1, b=2, c=3)

        f.assert_called_once_with(self, a=1, b=2, c=3, exception=e)

    def test_call_6(self):
        self._call_6(1, b=2)

        f.assert_called_once_with(self, 1, b=2, exception=e)

    def test_call_7(self):
        TestCall._call_7()

        f.assert_called_once_with(exception=e)

    def test_call_8(self):
        TestCall._call_8(1)

        f.assert_called_once_with(1, exception=e)

    def test_call_9(self):
        TestCall._call_9(a=1)

        f.assert_called_once_with(a=1, exception=e)

    def test_call_10(self):
        TestCall._call_10(a=1)

        f.assert_called_once_with(a=1, exception=e)

    def test_call_11(self):
        TestCall._call_11()

    def test_call_12(self):
        TestCall._call_12(1)

    def test_call_13(self):
        TestCall._call_13(a=1)

    @Catch(CatchError, f)
    def _call_1(self):
        raise e

    @Catch(CatchError, f)
    def _call_2(self, a):
        raise e

    @Catch(CatchError, f)
    def _call_3(self, a, b, c):
        raise e

    @Catch(CatchError, f)
    def _call_4(self, a):
        raise e

    @Catch(CatchError, f)
    def _call_5(self, a, b, c):
        raise e

    @Catch(CatchError, f)
    def _call_6(self, a, b):
        raise e

    @Catch(CatchError, f)
    def _call_7():
        raise e

    @Catch(CatchError, f)
    def _call_8(a):
        raise e

    @Catch(CatchError, f)
    def _call_9(a):
        raise e

    @Catch(CatchError, f)
    def _call_10(a=1):
        raise e

    @Catch(CatchError)
    def _call_11():
        raise e

    @Catch(CatchError)
    def _call_12(a):
        raise e

    @Catch(CatchError)
    def _call_13(a):
        raise e


if __name__ == "__main__":
    unittest.main()
