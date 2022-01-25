import unittest
from unittest import TestCase

from la_catch import catch


class CatchError(Exception):
    pass


class CatchMeTooError(Exception):
    pass


class TestCatch(TestCase):
    """
    Test catching exception(s).
    We go through every way the user can pass exception(s).
    Not passing exception is the same as catching Exception.
    """

    @catch()
    def test_catch_error_0(self):
        raise CatchError()

    @catch(CatchError)
    def test_catch_error_1(self):
        raise CatchError()

    @catch(exceptions=CatchError)
    def test_catch_error_2(self):
        raise CatchError()

    @catch((CatchError,))
    def test_catch_error_3(self):
        raise CatchError()

    @catch(exceptions=(CatchError,))
    def test_catch_error_4(self):
        raise CatchError()

    @catch((CatchError, CatchMeTooError))
    def test_catch_error_5(self):
        raise CatchError()

    @catch(exceptions=(CatchError, CatchMeTooError))
    def test_catch_error_6(self):
        raise CatchError()

    @catch((CatchError, CatchMeTooError))
    def test_catch_error_7(self):
        raise CatchMeTooError()

    @catch(exceptions=(CatchError, CatchMeTooError))
    def test_catch_error_8(self):
        raise CatchMeTooError()


if __name__ == "__main__":
    unittest.main()
