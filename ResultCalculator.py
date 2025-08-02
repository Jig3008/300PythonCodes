def calculateResult(marksDict):
    sumOfMarks = 0
    for k, v in marksDict.items():
        sumOfMarks += v
    return sumOfMarks, round((sumOfMarks/len(marksDict)),2)

try:
    marksDict = {}
    for i in range(1,7):
        subName = input('Enter the name of the subject:')
        marks = float(input('Enter the marks scored:'))
        marksDict[subName] = marks
    
    sumOfMarks, averageOfMarks = calculateResult(marksDict)
    print(f'The sum of all marks is {sumOfMarks} and average is {averageOfMarks}')
except:
    print('Program has an error')