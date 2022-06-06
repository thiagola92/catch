import unittest
from unittest import TestCase

from la_catch import Catch


class TestREADME(TestCase):
    """Test if exception is being ignored"""

    def test_readme(self):
        def func():
            with Catch(TypeError):
                raise TypeError("example")

        func()

        #######################################

        def on_error(exception):
            print(exception)

        def func():
            with Catch(TypeError, callback=on_error):
                raise TypeError("example")

        func()

        #######################################

        def on_error(message, exception):
            print(message, exception)

        def func():
            with Catch(TypeError, callback=on_error, message="WARNING:"):
                raise TypeError("example")

        func()

        #######################################

        def func():
            with Catch((TypeError, FileNotFoundError)):
                raise FileNotFoundError("example")

        func()

        #######################################

        @Catch(TypeError)
        def func():
            raise TypeError("example")

        func()

        #######################################

        @Catch(TypeError, callback=10)
        def func():
            raise TypeError("example")

        func()

        #######################################

        def on_error(exception):
            print(exception)

        @Catch(TypeError, callback=on_error)
        def func():
            raise TypeError("example")

        func()

        #######################################

        def on_error(message, exception):
            print(message, exception)

        @Catch(TypeError, callback=on_error, message="WARNING:")
        def func():
            raise TypeError("example")

        func()

        #######################################

        def on_error(message, exception):
            print(message, exception)

        @Catch(TypeError, callback=on_error)
        def func(message="WARNING:"):
            raise TypeError("example")

        func()

        #######################################

        def on_error(message, exception):
            print(message, exception)  # WARNING: example

        @Catch(TypeError, callback=on_error, message="warning:")
        def func(message="WARNING:"):
            raise TypeError("example")

        func()

        #######################################

        def on_error(exception):
            print(exception)  # not fake

        @Catch(TypeError, callback=on_error, exception="FAKE")
        def func(exception="fake"):
            raise TypeError("not fake")

        func()


if __name__ == "__main__":
    unittest.main()
