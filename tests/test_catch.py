import unittest
from unittest import TestCase

from catch import catch


class CatchError(Exception):
    pass


class CatchMeTooError(Exception):
    pass


class TestCatch(TestCase):
    @catch()
    def test_catch_error_0(self):
        raise CatchError("Test catching default exception and doing nothing")

    @catch(CatchError)
    def test_catch_error_1(self):
        raise CatchError("Test catching exception and doing nothing")

    @catch(exceptions=CatchError)
    def test_catch_error_2(self):
        raise CatchError("Test catching exception throught keyword and doing nothing")

    @catch((CatchError,))
    def test_catch_error_3(self):
        raise CatchError("Test catching exception inside a tuple and doing nothing")

    @catch(exceptions=(CatchError,))
    def test_catch_error_4(self):
        raise CatchError("Test catching exception inside a tuple throught keyword and doing nothing")

    @catch((CatchError, CatchMeTooError))
    def test_catch_error_5(self):
        raise CatchError("Test catching first exception and doing nothing")

    @catch(exceptions=(CatchError, CatchMeTooError))
    def test_catch_error_6(self):
        raise CatchError("Test catching first exception throught keyword and doing nothing")

    @catch((CatchError, CatchMeTooError))
    def test_catch_error_7(self):
        raise CatchMeTooError("Test catching second exception and doing nothing")

    @catch(exceptions=(CatchError, CatchMeTooError))
    def test_catch_error_8(self):
        raise CatchMeTooError("Test catching second exception throught keyword and doing nothing")

if __name__ == "__main__":
    unittest.main()
