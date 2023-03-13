from error_handler import error_handler_method
from my_mistake import MyCustomError

def calculate(num1, num2):
    result = num1 / num2
    if (num1 + num2 == 2):
        raise MyCustomError('Result 2!')

    return result

try:
    response = calculate(1, 0)
    print(response)
except Exception as exception:
    error_handler_method(exception)


# try:
#     num1 = 3
#     num2 = 0

#     response = num1 / num2

#     print(response)
# except NameError:
#     print('Esse valor não existe')
# except ZeroDivisionError:
#     print('Erro de divisão de zero!!!')
# except Exception as exception:
#     print(exception)
# finally:
#     print('Venha para K independentemente')
