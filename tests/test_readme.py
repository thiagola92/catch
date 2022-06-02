import unittest
from unittest import TestCase

from la_catch import Catch


class TestREADME(TestCase):
    """Test if exception is being ignored"""

    def test_readme(self):
        @Catch(Exception)
        def func():
            raise Exception()

        func()
        func()


if __name__ == "__main__":
    unittest.main()
