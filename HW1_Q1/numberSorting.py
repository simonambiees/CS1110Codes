# This programs takes in a series of numbers that user inputs and sorts them to find max and min and mean

# Asking for user input
blankCheck = input("This programs analyses a series of number inputs to find the Max, Min and Mean value.\nPlease type a number and hit enter to type the next.\nHit enter twice to start the analysis.\nONLY NUMBERS PLEASE!!!!or the program will crash!\n")

# initializing a list for containing user input
userInput = []
userInput.append(blankCheck)

# start of loop for checking if the user wants to end typing and storing inputs into a list.
while len(blankCheck) != 0:
    blankCheck = input()
    userInput.append(blankCheck)

# deleting the last empty element to avoid error when parsing str into float
userInput.pop(len(userInput)-1)

# soritng the elements in the list to find the max and min
for i in range(1, len(userInput)):
    for j in range(1, len(userInput)):
        if float(userInput[j]) > float(userInput[j-1]):
            temp = userInput[j]
            userInput[j] = userInput[j-1]
            userInput[j-1] = temp

# initializing sum and calculating sum for further calculation of mean
sum = 0.0
for i in userInput:
    sum += float(i)

# printing the results after calculating and aquiring max and min
print("The maximum of these numbers entered is " + userInput[0])
print("The minimum of these numbers entered is " + userInput[len(userInput)-1])
print("The mean of these numbers entered is " + str(sum/len(userInput)))

x = input("Press enter to exit")
