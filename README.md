# la-catch
Decorator and context manager to catch exception(s) and call a function to handle the error.  

# install
`pip install la-catch`  

# syntax
```python
Catch(exceptions, callback)
```
`exceptions` - Exception or Tuple of exceptions to be captured  
`callback` - function to be called in case of exceptions being raised **or** a return value to be returned in case of exceptions  
`**kwargs` - Any extra keywords are passed to callback

# context manager
Catch exception and do nothing:  
```python
from la_catch import Catch

def func():
    with Catch(TypeError):
        raise TypeError("example")
```

Catch exception and call callback passing exception:  
```python
from la_catch import Catch

def on_error(exception):
    print(exception)

def func():
    with Catch(TypeError, callback=on_error):
        raise TypeError("example")
```

Catch exception and call callback passing keywords arguments and exception:  
```python
from la_catch import Catch

def on_error(message, exception):
    print(message, exception)

def func():
    with Catch(TypeError, callback=on_error, message="WARNING:"):
        raise TypeError("example")
```

Catch multiple exceptions:  
```python
from la_catch import Catch

def func():
    with Catch((TypeError, FileNotFoundError)):
        raise FileNotFoundError("example")
```


# decorator
Catch exception and return `None`:  
```python
from la_catch import Catch

@Catch(TypeError)
def func():
    raise TypeError("example")
```

Catch exception and return a value:   
```python
from la_catch import Catch

@Catch(TypeError, callback=10)
def func():
    raise TypeError("example")
```

Catch exception and call callback passing exception:   
```python
from la_catch import Catch

def on_error(exception):
    print(exception)

@Catch(TypeError, callback=on_error)
def func():
    raise TypeError("example")
```

Catch exception and call callback passing keywords arguments and exception:   
```python
from la_catch import Catch

def on_error(message, exception):
    print(message, exception)

@Catch(TypeError, callback=on_error, message="WARNING:")
def func():
    raise TypeError("example")
```

Catch exception and call callback passing decorated function arguments and exception:   
```python
from la_catch import Catch

def on_error(message, exception):
    print(message, exception)

@Catch(TypeError, callback=on_error)
def func(message="WARNING:"):
    raise TypeError("example")
```

Function arguments have priority over initialization arguments:   
```python
from la_catch import Catch

def on_error(message, exception):
    print(message, exception) # WARNING: example

@Catch(TypeError, callback=on_error, message="warning:")
def func(message="WARNING:"):
    raise TypeError("example")
```

Exception have priority over function arguments and initialization arguments:   
```python
from la_catch import Catch

def on_error(exception):
    print(exception) # not fake

@Catch(TypeError, callback=on_error, exception="FAKE")
def func(exception="fake"):
    raise TypeError("not fake")
```