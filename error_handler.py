from my_mistake import MyCustomError

def error_handler_method(error):
    if isinstance(error, MyCustomError):
        print('Handle my custom error')
        return

    if isinstance(error, ZeroDivisionError):
        print('Treat division by zero')
        return

    if isinstance(error, Exception):
        print('Treat general case')
        return
