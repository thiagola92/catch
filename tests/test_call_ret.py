import unittest
from unittest import TestCase
from unittest.mock import Mock, create_autospec

from la_catch import catch


class CatchError(Exception):
    pass


def func(e, self):
    pass


f = create_autospec(func, return_value=10)
e = CatchError()


class TestCallRet(TestCase):
    """
    Test catching exception, calling function and returning a value.
    """

    def setUp(self) -> None:
        f.reset_mock()

        return super().setUp()

    def test_call_ret(self):
        r = self._call()

        assert r == 10
        
        f.assert_called_once_with(e, self)

    @catch(CatchError, f)
    def _call(self):
        raise e


if __name__ == "__main__":
    unittest.main()
