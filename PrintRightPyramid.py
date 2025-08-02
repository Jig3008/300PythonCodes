# Print a program using for loop to display below:
#     *
#     * *
#     * * *
#     * * * *
#     * * * * *

try:
    for i in range(0,6):
        for j in range(i):
            print("* ", end="")
        print("")
except:
    print('Program has an error!')