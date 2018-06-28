# This programs takes in a series of numbers that user inputs and sorts them to find max and min and mean

def getFirstInput():
    # Asking for user input of first matrix
    firstBlankCheck = input("This programs analyses a series of number inputs to find the Max, Min and Mean value.\nPlease type a number and hit enter to type the next.\nHit enter twice to start the analysis.\n\nEnter the first row numbers. Separate with a space. Hit enter for net row.\n\n")
    # Interpreting the user input
    firstNewRow = firstBlankCheck.split()
    # initializing a list for containing user input
    firstRowAndCol = []
    firstRowAndCol.append(firstNewRow)
    # start of loop for checking if the user wants to end typing and storing inputs into a list.
    while len(firstBlankCheck) != 0:
        firstBlankCheck = input()
        firstNewRow = firstBlankCheck.split()
        firstRowAndCol.append(firstNewRow)
    # deleting the last empty element to avoid error when parsing str into float
    firstRowAndCol.pop(len(firstRowAndCol)-1)
    return firstRowAndCol
def getSecondInput():
    # Asking for user input of second matrix
    secondBlankCheck = input("Enter the first row numbers. Separate with a space. Hit enter for net row.\n\n")
    #Interpreting the user input
    secondNewRow = secondBlankCheck.split()
    # initializing a list for containing user input
    secondRowAndCol = []
    secondRowAndCol.append(secondNewRow)
    # start of loop for checking if the user wants to end typing and storing inputs into a list.
    while len(secondBlankCheck) != 0:
        secondBlankCheck = input()
        secondNewRow = secondBlankCheck.split()
        secondRowAndCol.append(secondNewRow)
    # deleting the last empty element to avoid error when parsing str into float
    secondRowAndCol.pop(len(secondRowAndCol)-1)
    return secondRowAndCol


