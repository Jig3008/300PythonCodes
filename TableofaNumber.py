def printtable(inputNumber):
    for i in range(1,11):
        print(f'{inputNumber} * {i} = {inputNumber * i}')

try:
    inputNumber = int(input('Enter the number for which you want to print the math table:'))
    printtable(inputNumber)
except:
    print('Program has an error!')