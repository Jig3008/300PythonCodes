try:
    minMarks = 60
    studentMarks = float(input('Enter your marks:'))
    if studentMarks >= minMarks:
        print('Congratulations! You are eligible for the program!')
    elif studentMarks < minMarks:
        print(f'Sorry! You cannot take admission, you need {minMarks - studentMarks} marks more to take admission!')
except:
    print('Program has an error!')