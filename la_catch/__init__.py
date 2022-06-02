from asyncio import iscoroutinefunction
from typing import Any, Awaitable, Callable


class Catch:
    def __init__(
        self,
        exceptions: Exception | tuple[Exception] = Exception,
        callback: Callable | Awaitable | Any = None,
        *args,
        **kwargs,
    ):
        if not isinstance(exceptions, tuple):
            exceptions = (exceptions,)

        self._exceptions = exceptions
        self._callback = callback
        self._args = args
        self._kwargs = kwargs

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback) -> bool:
        if type not in self._exceptions:
            return False

        a, k = self._add_exception(self._args, self._kwargs, value)

        if callable(self._callback):
            self._callback(*a, **k)

        return True

    def __call__(self, func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except self._exceptions as e:
                a, k = self._create_temporary_arguments(args, kwargs)
                a, k = self._add_exception(a, k, e)

                if callable(self._callback):
                    return self._callback(*a, **k)
                return self._callback

        async def awrapper(*args, **kwargs):
            try:
                return await func(*args, **kwargs)
            except self._exceptions as e:
                a, k = self._create_temporary_arguments(args, kwargs)
                a, k = self._add_exception(a, k, e)

                if iscoroutinefunction(self._callback):
                    return await self._callback(*a, **k)
                elif callable(self._callback):
                    return self._callback(*a, **k)
                return self._callback

        if iscoroutinefunction(func):
            return awrapper
        return wrapper

    async def __aenter__(self):
        return self

    async def __aexit__(self, type, value, traceback) -> bool:
        if type not in self._exceptions:
            return False

        a, k = self._add_exception(self._args, self._kwargs, value)

        if callable(self._callback) and iscoroutinefunction(self._callback):
            await self._callback(*a, **k)
        elif callable(self._callback):
            self._callback(*a, **k)

        return True

    def _create_temporary_arguments(self, args, kwargs):
        """
        Create temporary arguments

        Changing directly self._args or self._kwargs
        would cause problems in subsequent calls from decorator,
        so you need to create copies every time.
        """

        return (args + self._args, kwargs | self._kwargs)

    def _add_exception(self, args, kwargs, exception):
        """
        Add exception to the arguments and return the new arguments to use

        Normally the exception is passed through kwargs,
        but i want to be usable with print() or logging.debug()
        and passing as kwargs would generate problems in this cases.
        """

        if kwargs:
            kwargs |= {"exception": exception}
        else:
            args = args + (exception,)

        return args, kwargs
