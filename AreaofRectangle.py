def calculateArea(length, width):
    return length * width


try:
    length = float(input('Enter the length of the rectangle:'))
    width = float(input('Enter the width of the rectangle:'))    
    print(f'Area of the rectangle is:{calculateArea(length, width)}')
except:
    print('Program has an error')