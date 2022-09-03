from la_catch import Catch


def warn(*args, **kwargs):
    print(args)


@Catch(Exception, callback=warn)
def Test(string: str) -> str:
    if not string:
        raise Exception(":(")
    return string


x = Test()
print(x)
