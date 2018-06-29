from gettingMatrices import *
from additionMatrices import *
from subtractMatrices import *


user_choice = input("Choose [1] if you would like to perform an addition\nChoose [2] if you would like to perform a subtraction\nChoose [3] if you would like to perform a multiplication\nThe two matrices should be of the same dimension!!!\n")

while True:
    if user_choice == "1":
        firstMatrix = get_first_input()
        secondMatrix = get_second_input()
        same_dimension = check_dimension(firstMatrix,secondMatrix)
        addition_matrix(firstMatrix,secondMatrix,same_dimension)
        break
    elif user_choice == "2":
        firstMatrix = get_first_input()
        secondMatrix = get_second_input()
        same_dimension = check_dimension(firstMatrix,secondMatrix)
        subtract_matrix(firstMatrix,secondMatrix,same_dimension)
        break
    elif user_choice == "3":
        #waiting
        print(" ")
        break
    else:
        print("Invalid input. Try again.")