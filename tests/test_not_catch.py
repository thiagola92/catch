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
    def test_not_catch_1(self):
        with self.assertRaises(DontCatchError):
            self._dont_catch_error_1()

    def test_not_catch_2(self):
        with self.assertRaises(DontCatchError):
            self._dont_catch_error_2()

    def test_not_catch_3(self):
        with self.assertRaises(DontCatchError):
            self._dont_catch_error_3()

    def test_not_catch_4(self):
        with self.assertRaises(DontCatchError):
            self._dont_catch_error_4()

    def test_not_catch_5(self):
        with self.assertRaises(DontCatchError):
            self._dont_catch_error_5()

    def test_not_catch_6(self):
        with self.assertRaises(DontCatchError):
            self._dont_catch_error_6()

    @catch(CatchError)
    def _dont_catch_error_1(self):
        raise DontCatchError("Test passing one exception that is never raised")

    @catch((CatchError,))
    def _dont_catch_error_2(self):
        raise DontCatchError(
            "Test passing one exception that is never raised inside a tuple"
        )

    @catch(exceptions=CatchError)
    def _dont_catch_error_3(self):
        raise DontCatchError(
            "Test passing one exception that is never raised throught keyword"
        )

    @catch(exceptions=(CatchError,))
    def _dont_catch_error_4(self):
        raise DontCatchError(
            "Test passing one exception that is never raised inside a tuple throught keyword"
        )

    @catch((CatchError, CatchMeTooError))
    def _dont_catch_error_5(self):
        raise DontCatchError(
            "Test passing two exceptions that are never raised inside a tuple"
        )

    @catch(exceptions=(CatchError, CatchMeTooError))
    def _dont_catch_error_6(self):
        raise DontCatchError(
            "Test passing two exceptions that are never raised inside a tuple throught keyword"
        )


if __name__ == "__main__":
    unittest.main()
