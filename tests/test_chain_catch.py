import unittest
from unittest import TestCase
from unittest.mock import Mock

from la_catch import catch


class CatchError(Exception):
    pass


e1 = CatchError()
e2 = CatchError()


class TestChainCatch(TestCase):
    """
    Test catch after other catch happen.
    """

    def test_chain_catch(self):
        self._call_first()

    @catch(CatchError)
    def _call_second(e, self):
        raise e2

    @catch(CatchError, _call_second)
    def _call_first(self):
        raise e1


if __name__ == "__main__":
    unittest.main()
