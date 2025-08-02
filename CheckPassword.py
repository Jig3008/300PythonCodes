#Check if the entered password is only alphanumeric and not greater than equal to 8
#if we wanted to check just numeric - use isnumeric()
#just alphabets - use isalpha()

def checkPassword(inputPassword):
    return (inputPassword.isalnum() and (len(inputPassword)) <= 8)

try:
    inputPassword = input('Enter your password:')
    if checkPassword(inputPassword) == True:
        print('Congratulations! Your password is alphanumeric!')
    else:
        print('Our system does not allow password of length greater than 8 characters or special characters or whitespaces!')
except:
    print('Program has an error')