import unittest
from unittest import TestCase
from unittest.mock import Mock

from catch import catch


class CatchError(Exception):
    pass


function = Mock()
first_error = CatchError()
second_error = CatchError()


class TestChainCall(TestCase):
    def setUp(self) -> None:
        function.reset_mock(return_value=True, side_effect=True)

        return super().setUp()
    
    def test_chain_call(self):
        self._call_first()

        function.assert_called_once_with(second_error, first_error, self)
    
    @catch(CatchError, function)
    def _call_second(e, self):
        raise second_error

    @catch(CatchError, _call_second)
    def _call_first(self):
        raise first_error


if __name__ == "__main__":
    unittest.main()
