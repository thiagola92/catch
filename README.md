# catch
Decorator to catch exception(s) and call function to handle the error. Can also define a return value to the function after catching.  
There is no benifits from using this decorator other than letting the code more readable (arguable).  

# install
`pip install git+https://github.com/thiagola92/catch#egg=catch`

# syntax
```python
@catch(exceptions, call, ret)
```
`exceptions` - Exception or Tuple of exceptions to be captured  
`call` - function to be called in case of exceptions being raised  
`ret` - value to be returned by the main function in case of exceptions being raised  

In case an exception is raised and no `ret` was defined, the return will be the same that `call` would return.  

# example
```python
@catch(Timeout, logging.exception, ret=[])
def scrap_details(url):
    response = requests.get("https://www.amazon.com/dp/B00YFTHJ9C")
    selector = Selector(text=response.content)

    return selector.xpath('//li[@class="swatchAvailable"]//div[@class="twisterSlotDiv "]').getall()
```

# usages
No `Exception` will be raise and `None` will be returned.  
```python
@catch(Exception)
def example():
    # code here
```

No `Exception` will be raise and `func` will be called with the exception.  
```python
def func(e):
    print("Exception raised: ", e)


@catch(Exception, func)
def example():
    # code here
```

No `Exception` will be raise, `func` will be called with the exception and `False` will be returned by `example()`.  
```python
def func(e):
    print("Exception raised: ", e)

    return False


@catch(Exception, func)
def example():
    # code here
```

No `Exception` will be raise, `func` will be called with the exception and `False` will be returned by `example()`.  
```python
def func(e):
    print("Exception raised: ", e)


@catch(Exception, func, False)
def example():
    # code here
```
