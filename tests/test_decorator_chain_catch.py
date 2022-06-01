import unittest
from unittest import TestCase
from unittest.mock import Mock

from la_catch import Catch


class CatchError(Exception):
    pass


e1 = CatchError()
e2 = CatchError()


class TestDecoratorChainCatch(TestCase):
    """
    Test catching after other catch happen.
    """

    def test_chain_catch(self):
        self._call_first()

    @Catch(CatchError)
    def _call_second(self, exception):
        raise e2

    @Catch(CatchError, _call_second)
    def _call_first(self):
        raise e1


if __name__ == "__main__":
    unittest.main()
