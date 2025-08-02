try:
    squareAndCubesDict = {}
    for i in range(1,6):
        squareAndCubesDict[i] = [i*i,i*i*i]
    print('Number\t\t\t\tSquare\t\t\t\tCube')
    for k,v in squareAndCubesDict.items():
        print(f'{k}\t\t\t\t{v[0]}\t\t\t\t{v[1]}')
except:
    print('Program has a fault')