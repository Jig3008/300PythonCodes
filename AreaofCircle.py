from math import pi

def calculateArea(radius):
    return pi * radius * radius


try:
    radiusInput = float(input('Enter the radius to calculate the area:'))
    print(f'Area of the circle is: {round(calculateArea(radiusInput),2)}')
except:
    print('Program has an error')