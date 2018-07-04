import gettingMatrices
import gettingVectors
import additionMatrices
import subtractMatrices
import transposeMatrix
import multiplyMatrices
import Menu
import multiplyVectorAndMartix


def main():
    print("Choose [1] if you would like to perform a matrix addition")
    print("Choose [2] if you would like to perform a matrix subtraction")
    print("Choose [3] if you would like to perform a matrix multiplication")
    print("The two matrices should be of the same dimension!!!\n\n")
    print("Choose [4] if you would like to get a tranpose of a matrix")
    print("Choose [5] if you would like to multiply a vector by a matrix")
    print("The vector must have the dimension same as the Col number of matrix")
    user_choice = input("Your choice is: ")

    while True:
        # case when user chooses addition function
        if user_choice == "1":
            inputs = gettingMatrices.get_input(2)
            firstMatrix = inputs[0]
            secondMatrix = inputs[1]
            same_dimension = gettingMatrices.check_dimension(firstMatrix,secondMatrix, False)
            additionMatrices.addition_matrix(firstMatrix,secondMatrix,same_dimension)
            next_choice = input("Type Y(yes) to execute program again.\nType N(no) to exit.")
            if next_choice == "Y":
                Menu.jump()
            elif next_choice == "N":
                break
    
        # case when user chooses subtraction function
        elif user_choice == "2":
            inputs = gettingMatrices.get_input(2)
            firstMatrix = inputs[0]
            secondMatrix = inputs[1]
            same_dimension = gettingMatrices.check_dimension(firstMatrix,secondMatrix, False)
            subtractMatrices.subtract_matrix(firstMatrix,secondMatrix,same_dimension)
            next_choice = input("Type Y(yes) to execute program again.\nType N(no) to exit.")
            if next_choice == "Y":
                Menu.jump()
            elif next_choice == "N":
                break
    
        # case when user chooses multiply function
        elif user_choice == "3":
            inputs = gettingMatrices.get_input(2)
            firstMatrix = inputs[0]
            secondMatrix = inputs[1]
            proper_dimension = gettingMatrices.check_dimension(firstMatrix, secondMatrix, True)
            multiplyMatrices.multi_matrix(firstMatrix, secondMatrix, proper_dimension)
            next_choice = input("Type Y(yes) to execute program again.\nType N(no) to exit.")
            if next_choice == "Y":
                Menu.jump()
            elif next_choice == "N":
                break
        
        # case when user chooses transpose function
        elif user_choice == "4":
            firstMatrix = gettingMatrices.get_input(1)
            transposeMatrix.to_transpose(firstMatrix,True)
            next_choice = input("Type Y(yes) to execute program again.\nType N(no) to exit.")
            if next_choice == "Y":
                Menu.jump()
            elif next_choice == "N":
                break
        
        elif user_choice == "5":
            user_vector = gettingVectors.get_input(1)
            user_matrix = gettingMatrices.get_input(1)
            same_dimension = gettingVectors.check_length(user_vector,user_matrix)
            multiplyVectorAndMartix.multiply(user_vector, user_matrix, same_dimension)
            next_choice = input("Type Y(yes) to execute program again.\nType N(no) to exit.")
            if next_choice == "Y":
                Menu.jump()
            elif next_choice == "N":
                break
        else:
            print("Invalid input. Try again.")
            
main()
