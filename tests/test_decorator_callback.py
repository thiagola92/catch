import unittest
from unittest import TestCase

from la_catch import Catch


class CatchError(Exception):
    pass


class TestDecoratorCallback(TestCase):
    """Test catching exception and callback."""

    def test_callback(self):
        self._call()

    def catched(self, exception):
        assert isinstance(exception, CatchError)

    @Catch(CatchError, catched)
    def _call(self):
        raise CatchError("Catch me")


if __name__ == "__main__":
    unittest.main()
