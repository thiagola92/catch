from asyncio import iscoroutinefunction
from typing import Any, Awaitable, Callable

from la_catch.utility import get_arguments


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

        self.ret = None

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback) -> bool:
        if type not in self._exceptions:
            return False

        self._kwargs |= {"exception": value}

        if callable(self._callback):
            self.ret = self._callback(*self._args, **self._kwargs)
        else:
            self.ret = self._callback

        return True

    def __call__(self, func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            args, kwargs = get_arguments(func=func, args=args, kwargs=kwargs)

            a = args + self._args
            k = kwargs | self._kwargs

            with self.__class__(self._exceptions, self._callback, *a, **k) as catch:
                return func(*args, **kwargs)
            return catch.ret

        async def awrapper(*args, **kwargs):
            args, kwargs = get_arguments(func=func, args=args, kwargs=kwargs)

            a = args + self._args
            k = kwargs | self._kwargs

            async with self.__class__(
                self._exceptions, self._callback, *a, **k
            ) as catch:
                return await func(*args, **kwargs)
            return catch.ret

        if iscoroutinefunction(func):
            return awrapper
        return wrapper

    async def __aenter__(self):
        return self

    async def __aexit__(self, type, value, traceback) -> bool:
        if type not in self._exceptions:
            return False

        self._kwargs |= {"exception": value}

        if callable(self._callback) and iscoroutinefunction(self._callback):
            self.ret = await self._callback(*self._args, **self._kwargs)
        elif callable(self._callback):
            self.ret = self._callback(*self._args, **self._kwargs)

        return True
