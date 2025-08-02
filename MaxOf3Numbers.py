def maxNumber(number1, number2, number3):
    result = float()
    if number1 > number2:
        if number1 > number3:
            result = number1
        else:
            result = number3
    elif number2 > number3:
        result = number2
    else:
        result = number3
    return result

try:
    numberList = []
    for i in range(0,3):
        numberInput = float(input('Enter the number:'))
        numberList.append(numberInput)
    print(f'Maximum of the 3 numbers is:{maxNumber(numberList[0],numberList[1],numberList[2])}')
    print(f'The max of the number using max function is:{max(numberList[0],numberList[1],numberList[2])}')
except:
    print('Program has an error!')