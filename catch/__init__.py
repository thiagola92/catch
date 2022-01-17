def do_nothing(*args, **kwargs):
    return None


def catch(exceptions: Exception | tuple = Exception, call=do_nothing):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exceptions as exception:
                return call(exception, *args, **kwargs)

        return wrapper

    return decorator
