import unittest
from unittest import TestCase

from catch import catch


class DontCatchError(Exception):
    pass


class CatchError(Exception):
    pass


class CatchMeTooError(Exception):
    pass


class TestNotCatch(TestCase):
    """
    Test not catching unwanted exceptions.
    We go through every way the user can pass exception(s).
    """

    def test_not_catch_1(self):
        with self.assertRaises(DontCatchError):
            self._call_1()

    def test_not_catch_2(self):
        with self.assertRaises(DontCatchError):
            self._call_2()

    def test_not_catch_3(self):
        with self.assertRaises(DontCatchError):
            self._call_3()

    def test_not_catch_4(self):
        with self.assertRaises(DontCatchError):
            self._call_4()

    def test_not_catch_5(self):
        with self.assertRaises(DontCatchError):
            self._call_5()

    def test_not_catch_6(self):
        with self.assertRaises(DontCatchError):
            self._call_6()

    @catch(CatchError)
    def _call_1(self):
        raise DontCatchError()

    @catch((CatchError,))
    def _call_2(self):
        raise DontCatchError()

    @catch(exceptions=CatchError)
    def _call_3(self):
        raise DontCatchError()

    @catch(exceptions=(CatchError,))
    def _call_4(self):
        raise DontCatchError()

    @catch((CatchError, CatchMeTooError))
    def _call_5(self):
        raise DontCatchError()

    @catch(exceptions=(CatchError, CatchMeTooError))
    def _call_6(self):
        raise DontCatchError()


if __name__ == "__main__":
    unittest.main()
