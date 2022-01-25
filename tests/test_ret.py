import unittest
from unittest import TestCase

from catch import catch


class CatchError(Exception):
    pass


e = CatchError()


class TestRet(TestCase):
    """
    Test catching exception and returning a value.
    """

    def test_ret_1(self):
        assert self._call_1() == 10

    def test_ret_2(self):
        assert self._call_2() == 10.0

    def test_ret_3(self):
        assert self._call_3() == "10"

    def test_ret_4(self):
        assert self._call_4() == e

    @catch(CatchError, ret=10)
    def _call_1(self):
        raise e

    @catch(CatchError, ret=10.0)
    def _call_2(self):
        raise e

    @catch(CatchError, ret="10")
    def _call_3(self):
        raise e

    @catch(CatchError, ret=e)
    def _call_4(self):
        raise e


if __name__ == "__main__":
    unittest.main()
