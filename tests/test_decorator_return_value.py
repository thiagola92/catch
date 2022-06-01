import unittest
from unittest import TestCase

from la_catch import Catch


class CatchError(Exception):
    pass


class TestDecoratorReturnValue(TestCase):
    """Test catching exception and returning a value."""

    def test_return_value(self):
        r = self._call()

        assert r == 10

    @Catch(CatchError, 10)
    def _call(self):
        raise CatchError("Catch me")


if __name__ == "__main__":
    unittest.main()
