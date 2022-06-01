import unittest
from unittest import TestCase

from la_catch import Catch


class CatchError(Exception):
    pass


class CatchMeTooError(Exception):
    pass


class TestDecoratorCatch(TestCase):
    """
    Test catching exception(s).
    We go through every way the user can pass exception(s).
    Not passing exception is the same as catching Exception.
    """

    @Catch()
    def test_catch_error_0(self):
        raise CatchError()

    @Catch(CatchError)
    def test_catch_error_1(self):
        raise CatchError()

    @Catch(exceptions=CatchError)
    def test_catch_error_2(self):
        raise CatchError()

    @Catch((CatchError,))
    def test_catch_error_3(self):
        raise CatchError()

    @Catch(exceptions=(CatchError,))
    def test_catch_error_4(self):
        raise CatchError()

    @Catch((CatchError, CatchMeTooError))
    def test_catch_error_5(self):
        raise CatchError()

    @Catch(exceptions=(CatchError, CatchMeTooError))
    def test_catch_error_6(self):
        raise CatchError()

    @Catch((CatchError, CatchMeTooError))
    def test_catch_error_7(self):
        raise CatchMeTooError()

    @Catch(exceptions=(CatchError, CatchMeTooError))
    def test_catch_error_8(self):
        raise CatchMeTooError()


if __name__ == "__main__":
    unittest.main()
