import gettingMatrices
import additionMatrices
import subtractMatrices
import transposeMatrix
import multiplyMatrices



user_choice = input("Choose [1] if you would like to perform an addition\nChoose [2] if you would like to perform a subtraction\nChoose [3] if you would like to perform a multiplication\nChoose [4] if you would like to get a tranpose\nThe two matrices should be of the same dimension!!!\n")

while True:
    # case when user chooses addition function
    if user_choice == "1":
        inputs = gettingMatrices.get_input(2)
        firstMatrix = inputs[0]
        secondMatrix = inputs[1]
        same_dimension = gettingMatrices.check_dimension(firstMatrix,secondMatrix, False)
        additionMatrices.addition_matrix(firstMatrix,secondMatrix,same_dimension)
        break
    
    # case when user chooses subtraction function
    elif user_choice == "2":
        inputs = gettingMatrices.get_input(2)
        firstMatrix = inputs[0]
        secondMatrix = inputs[1]
        same_dimension = gettingMatrices.check_dimension(firstMatrix,secondMatrix, False)
        subtractMatrices.subtract_matrix(firstMatrix,secondMatrix,same_dimension)
        break
    
    # case when user chooses transpose function
    elif user_choice == "3":
        inputs = gettingMatrices.get_input(2)
        firstMatrix = inputs[0]
        secondMatrix = inputs[1]
        proper_dimension = gettingMatrices.check_dimension(firstMatrix, secondMatrix, True)
        multiplyMatrices.multi_matrix(firstMatrix, secondMatrix, proper_dimension)
        break
        
    # case when user chooses multiplication function
    elif user_choice == "4":
        firstMatrix = gettingMatrices.get_input(1)
        transposeMatrix.to_transpose(firstMatrix,True)
        break
    else:
        print("Invalid input. Try again.")
