try:
    squaredDict = {}
    for i in range(1,6):
        squaredDict[i] = i * i

    print('Number\t\t\t\tSquare')
    for k, v in squaredDict.items():
        print(f'{k}\t\t\t\t{v}')
except:
    print('The program is having a fault')


