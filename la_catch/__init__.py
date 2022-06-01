from asyncio import iscoroutinefunction
from typing import Any, Awaitable, Callable


def catch(
    exceptions: Exception | tuple = Exception,
    call: Callable = lambda *args, **kwargs: None,
    ret: Any = ...,
    include_args: bool = True,
):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exceptions as exception:
                if include_args:
                    call_return = call(*args, exception, **kwargs)
                else:
                    call_return = call(exception)

                if ret is not Ellipsis:
                    return ret

                return call_return

        return wrapper

    return decorator


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
            try:
                return func(*args, **kwargs)
            except self._exceptions as e:
                a = args + self._args
                k = kwargs | self._kwargs | {"exception": e}

                if callable(self._callback):
                    return self._callback(*a, **k)
                return self._callback

        async def awrapper(*args, **kwargs):
            try:
                return await func(*args, **kwargs)
            except self._exceptions as e:
                a = args + self._args
                k = kwargs | self._kwargs | {"exception": e}

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

        self._kwargs |= {"exception": value}

        if callable(self._callback) and iscoroutinefunction(self._callback):
            await self._callback(*self._args, **self._kwargs)
        elif callable(self._callback):
            self._callback(*self._args, **self._kwargs)

        return True
