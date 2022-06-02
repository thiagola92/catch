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

# basic
`Catch` exist to create a reaction to a exception, the idea is to split the logic that deals with error from the main logic.   

Normally you would ignore an exception like this:

```python
def func():
    try:
        raise TypeError()
    except TypeError:
        pass
```

But using `Catch` you could ignore using *context manager* or a *decorator*.  

```python
from la_catch import Catch

def func():
    with Catch(TypeError)
        raise TypeError()
```

```python
from la_catch import Catch

@Catch(TypeError)
def func():
    raise TypeError()
```

# callback
Pass a callback to be invoked when the error occurs.  

```python
def on_error(exception):
    print("Let me try to solve the exception: ", exception)

with Catch(TypeError, on_error)
    raise TypeError()
```

```python
def on_error(exception):
    print("Let me try to solve the exception: ", exception)

@Catch(TypeError, on_error)
def func():
    raise TypeError()

func()
```

# callback arguments
Any extra argument giving during initialization will be passed to the callback when the erro occurs.  

```python
def on_error(name, exception):
    print(f"Hi {name}! Look what i found:", exception)

with Catch(TypeError, on_error, "alice")
    raise TypeError()
```

```python
def on_error(name, exception):
    print(f"Hi {name}! Look what i found:", exception)

@Catch(TypeError, on_error, "alice")
def func():
    raise TypeError()

func()
```

Exception will come as keyword argument or as last argument if there is no keyword arguments.  

**Recomendation**: If you always assume that exception will come as keyword argument called `exception` you will be fine.  

# decorator
Decorators are more complex for two reasons:
- Decorated function still needs to return a value
- Decorated function will receive the functions arguments

As said, the callback will receive the same values that decorated function received.  

```python
def on_error(value, exception):
    print("Your input value is invalid, value:", value)
    print("We will be giving 1 to you")
    return 1

@Catch(ValueError, on_error)
def get_money(value):
    return int(value) + 1

money = get_money("i want my money")
print("This is how much money you will get:", money)
```