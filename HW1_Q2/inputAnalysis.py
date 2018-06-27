# This program takes in multiple lines of user input and analyese the frequency of each English letter appearing.

# first line of input & also a string for checking if the user is done typing.
blankCheck = input("Welcome!\nThis program takes in MULTIPLE lines of user input and analyses the frequency of letters appering.\nPlease limit your input to all the characters on a !!!NORMAL LAPTOP KEYBOARD!!!\nStart typing below when you\'re ready.\n")

# Initializing userInput var
userInput = blankCheck

# Initializing the countOfAppearing var
countOfAppearing = 0

# Initializing a list for regularly used characters that can be typed on a keyboard
checkList = ["  "," ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0","`",",",".","/","'",";","[","]","-","=","!","@","#","$","%","^","&","*","(",")","_","+","{","}","|",":","\"","<",">","?","~","\\"]

# start of loop for checking if the user wants to end typing.
while len(blankCheck) != 0:
    blankCheck = input()
    userInput += blankCheck
    userInput = userInput.lower()

# debug line for printing user input
# print(userInput)

# initializing the list for results
resultList = []

# for loop to calculate the frequencies and storing them in list
for j in range(0, len(checkList)):
    # Initializing the countOfAppearing var
    countOfAppearing = 0
    # initializing the frequency var
    frequency = 0
    for i in range(0, len(userInput)):
        if userInput[i] == checkList[j]:
            countOfAppearing += 1
            # frequency = float(countOfAppearing)/len(userInput)
            frequency = countOfAppearing
    if countOfAppearing >0:
        resultList.append("CHARACTER: " + "\"" + str(checkList[j]) + "\"" + "   " + "FREQUENCY: " + str(frequency))


# sorting the frequencies in descending order
temp = "" #temp var for exchanging elements
count = len(resultList)-1 #count for deciding whether to continue sorting
while count > 0:
    for i in range(1,len(resultList)):
        if float(resultList[i][27:len(resultList[i])])> float(resultList[i-1][27:len(resultList[i-1])]):
            temp = resultList[i]
            resultList[i] = resultList[i-1]
            resultList[i-1] = temp
    count -= 1

# printing the elements in the list each on a separate line
if len(resultList>0):
    print("Results are in DESCENDING order!!!!!")
    for i in resultList:
        print(i)
else:
    print("No characters entered!")





