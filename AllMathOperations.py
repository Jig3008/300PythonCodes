def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def modulo(a,b):
    if a >= b:
        return a%b

try:
    print('Enter the numbers to carry out all math operations')
    number1 = float(input('Enter number 1:'))
    number2 = float(input('Enter number 2:'))
    print(f'Addition of the numbers is {add(number1, number2)}')
    print(f'Subtraction of the numbers is {sub(number1, number2)}')
    print(f'Multiplication of the numbers is {mul(number1, number2)}')
    print(f'Division of the numbers is {div(number1, number2)}')
    print(f'Modulo of the numbers is {modulo(number1, number2)}')                
except:
    print('Program has an error!')