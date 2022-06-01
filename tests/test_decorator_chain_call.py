import unittest
from unittest import TestCase
from unittest.mock import Mock

from la_catch import catch


class CatchError(Exception):
    pass


f = Mock()
e1 = CatchError()
e2 = CatchError()


class TestDecoratorChainCall(TestCase):
    """Test catching and calling a function after other catch happen."""

    def setUp(self) -> None:
        f.reset_mock(return_value=True, side_effect=True)

        return super().setUp()

    def test_chain_call(self):
        self._call_first()

        f.assert_called_once_with(self, e1, e2)

    @catch(CatchError, f)
    def _call_second(self, e):
        raise e2

    @catch(CatchError, _call_second)
    def _call_first(self):
        raise e1


if __name__ == "__main__":
    unittest.main()
