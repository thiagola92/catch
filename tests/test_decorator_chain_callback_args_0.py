import unittest
from unittest import TestCase

from la_catch import Catch


class TestDecorator(TestCase):
    """Test if is possible to chain Catchs"""

    def setUp(self) -> None:
        self._type_error = TypeError()
        self._file_not_found = FileNotFoundError()

    def test_decorator(self):
        m1 = "File fail"
        m2 = "Type fail"

        def on_file_error(message1, exception):
            assert message1 == m1
            assert exception == self._file_not_found

        def on_type_error(message2, exception):
            assert message2 == m2
            assert exception == self._type_error

        @Catch(FileNotFoundError, callback=on_file_error, message1=m1)
        @Catch(TypeError, callback=on_type_error, message2=m2)
        def func():
            raise self._type_error

        func()
        func()

    def test_decorator(self):
        m1 = "File fail"
        m2 = "Type fail"

        def on_file_error(message1, exception):
            assert message1 == m1
            assert exception == self._file_not_found

        def on_type_error(message2, exception):
            assert message2 == m2
            assert exception == self._type_error

        @Catch(FileNotFoundError, callback=on_file_error, message1=m1)
        @Catch(TypeError, callback=on_type_error, message2=m2)
        def func():
            raise self._file_not_found

        func()
        func()


if __name__ == "__main__":
    unittest.main()
