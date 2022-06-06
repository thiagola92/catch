from asyncio import iscoroutinefunction
from inspect import signature
from typing import Any, Awaitable, Callable


class Catch:
    def __init__(
        self,
        exceptions: Exception | tuple[Exception] = Exception,
        callback: Callable | Awaitable | Any = None,
        **kwargs,
    ):
        if not isinstance(exceptions, tuple):
            exceptions = (exceptions,)

        self._exceptions = exceptions
        self._callback = callback
        self._kwargs = kwargs

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback) -> bool:
        if type not in self._exceptions:
            return False

        k = self._kwargs | {"exception": value}

        if callable(self._callback):
            self._callback(**k)

        return True

    def __call__(self, func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except self._exceptions as e:
                k = self._get_decorator_arguments(func, args, kwargs, e)

                if callable(self._callback):
                    return self._callback(**k)
                return self._callback

        async def awrapper(*args, **kwargs):
            try:
                return await func(*args, **kwargs)
            except self._exceptions as e:
                k = self._get_decorator_arguments(func, args, kwargs, e)

                if iscoroutinefunction(self._callback):
                    return await self._callback(**k)
                elif callable(self._callback):
                    return self._callback(**k)
                return self._callback

        if iscoroutinefunction(func):
            return awrapper
        return wrapper

    async def __aenter__(self):
        return self

    async def __aexit__(self, type, value, traceback) -> bool:
        if type not in self._exceptions:
            return False

        k = self._kwargs | {"exception": value}

        if callable(self._callback) and iscoroutinefunction(self._callback):
            await self._callback(**k)
        elif callable(self._callback):
            self._callback(**k)

        return True

    def _get_decorator_arguments(
        self, func: Callable, args: tuple, kwargs: dict, exception: Exception
    ) -> dict[str, Any]:
        """
        Get the arguments for the decorator.

        Keyword priority:
            1. Keyword 'exception'
            2. Arguments from decorated function
            3. Initialization keywords arguments
        """

        # Replicate the arguments received by decorated function
        sign = signature(func)
        bound_arguments = sign.bind(*args, **kwargs)
        bound_arguments.apply_defaults()
        arguments = bound_arguments.arguments

        # Apply priority
        arguments = self._kwargs | arguments | {"exception": exception}

        return arguments
