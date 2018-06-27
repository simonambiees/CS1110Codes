# This programs takes in a series of numbers that user inputs and sorts them to find max and min and mean

blankCheck = input("This programs analyses a series of number inputs to find the Max, Min and Mean value.\nPlease type a number and hit enter to type the next.\nHit enter twice to start the analysis.\n")
userInput = []
userInput.append(blankCheck)
# start of loop for checking if the user wants to end typing and storing inputs into a list.
while len(blankCheck) != 0:
    blankCheck = input()
    userInput.append(blankCheck)

for i in range(1, len(userInput)):
    for j in range(1, len(userInput)):
        if float(userInput[j]) > float(userInput[j-1]):
            temp = userInput[j]
            userInput[j] = userInput[j-1]
            userInput[j-1] = temp

sum = 0.0
for i in userInput:
    sum += float(i)


print("The maximum of these numbers entered is " + float(userInput[0]))
print("The minimum of these numbers entered is " + float(userInput[len(userInput)-1]))
print("The mean of these numbers entered is " + sum/len(userInput))
