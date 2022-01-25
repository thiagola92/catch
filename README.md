# catch
Decorator to catch exception(s) and call function to handle the error. Can also define a return value to the function after catching.  
There is no benifits from using this decorator other than letting the code more readable (arguable).  

# install
`pip install git+https://github.com/thiagola92/catch#egg=catch`

# example

## direct approach
```python
@catch(Timeout, logging.exception, ret=[])
def scrap_details(url):
    response = requests.get("https://www.amazon.com/dp/B00YFTHJ9C")
    selector = Selector(text=response.content)

    return selector.xpath('//li[@class="swatchAvailable"]//div[@class="twisterSlotDiv "]').getall()
```
