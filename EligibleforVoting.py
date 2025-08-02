try:
    legalAge = 18
    age = int(input('Enter your age:'))
    if age >= legalAge:
        print('You can vote')
    elif age < 18:
        print(f'Sorry! You cannot participate in voting, you would be able to participate after {legalAge - age} years')
except:
    print('Program has an error!')