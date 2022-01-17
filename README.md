# catch
Decorator to catch exceptions and map to functions call. There is no benifits from using this decorator other than letting the code more readable (arguable).

# install
`pip install git+https://github.com/thiagola92/catch#egg=catch`

# example

## direct approach
```python
def scrap_product(url):
    try:
        # request product
        # parse product
        # return product
    except Exception as e:
        # logging
        # error treatment
```

## split logic with function
```python
def treatment(url, exception):
    # logging
    # error treatment

def scrap_product(url):
    try:
        # request product
        # parse product
        # return product
    except Exception as e:
        treatment(url=url, exception=e)
```

## split logic with decorator
```python
from catch import catch

def treatment(exception, url): # notice that exception is the first arg
    # logging
    # error treatment

@catch(Exception, treatment)
def scrap_product(url):
    # request product
    # parse product
    # return product
```
