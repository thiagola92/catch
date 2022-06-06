from asyncio import iscoroutinefunction
from inspect import Signature, signature
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

        self._kwargs |= {"exception": value}

        if callable(self._callback):
            self._callback(*self._args, **self._kwargs)

        return True

    def __call__(self, func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            sign = signature(func)
            bound_arguments = sign.bind(*args, **kwargs)
            bound_arguments.apply_defaults()
            args = bound_arguments.args
            kwargs = bound_arguments.kwargs

            try:
                return func(*args, **kwargs)
            except self._exceptions as e:
                if callable(self._callback):
                    kwargs |= {"exception": e}
                    return self._callback(*args, **kwargs)
                return self._callback

        async def awrapper(*args, **kwargs):
            sign = signature(func)
            bound_arguments = sign.bind(*args, **kwargs)
            bound_arguments.apply_defaults()
            args = bound_arguments.args
            kwargs = bound_arguments.kwargs

            try:
                return await func(*args, **kwargs)
            except self._exceptions as e:
                if iscoroutinefunction(self._callback):
                    kwargs |= {"exception": e}
                    return await self._callback(*args, **kwargs)
                elif callable(self._callback):
                    kwargs |= {"exception": e}
                    return self._callback(*args, **kwargs)
                return self._callback

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
            await self._callback(*self._args, **self._kwargs)
        elif callable(self._callback):
            self._callback(*self._args, **self._kwargs)

        return True
