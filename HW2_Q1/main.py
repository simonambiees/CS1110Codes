import gettingMatrices
import gettingVectors
import additionMatrices
import subtractMatrices
import transposeMatrix
import multiplyMatrices
import multiplyVectorAndMartix
import symmetryTest
import vectorDotProduct
import weightedDotProduct


def main():
    print("Choose [1] if you would like to perform a matrix addition")
    print("Choose [2] if you would like to perform a matrix subtraction")
    print("Choose [3] if you would like to perform a matrix multiplication")
    print("The two matrices should be of the same dimension!!!\n\n")
    print("Choose [4] if you would like to get a tranpose of a matrix")
    print("Choose [5] if you would like to check if a matrix is symmetric")
    print("Choose [6] if you would like to multiply a vector by a matrix")
    print("Choose [7] if you would like to calculate dot product of two vectors")
    print("Choose [8] if you would like to calculate weighted dot product of two vectors")
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
            next_choice = input("Type y(yes) to execute program again.\nType anything else to exit. ")
            if next_choice == "y":
                main()
            elif next_choice == "n":
                raise SystemExit
            else:
                raise SystemExit
    
        # case when user chooses subtraction function
        elif user_choice == "2":
            inputs = gettingMatrices.get_input(2)
            firstMatrix = inputs[0]
            secondMatrix = inputs[1]
            same_dimension = gettingMatrices.check_dimension(firstMatrix, secondMatrix, False)
            subtractMatrices.subtract_matrix(firstMatrix, secondMatrix, same_dimension)
            next_choice = input("Type y(yes) to execute program again.\nType anything else to exit. ")
            if next_choice == "y":
                main()
            elif next_choice == "n":
                raise SystemExit
            else:
                raise SystemExit
    
        # case when user chooses multiply function
        elif user_choice == "3":
            inputs = gettingMatrices.get_input(2)
            firstMatrix = inputs[0]
            secondMatrix = inputs[1]
            proper_dimension = gettingMatrices.check_dimension(firstMatrix, secondMatrix, True)
            multiplyMatrices.multi_matrix(firstMatrix, secondMatrix, proper_dimension)
            next_choice = input("Type y(yes) to execute program again.\nType anything else to exit. ")
            if next_choice == "y":
                main()
            elif next_choice == "n":
                raise SystemExit
            else:
                raise SystemExit
        
        # case when user chooses transpose function
        elif user_choice == "4":
            firstMatrix = gettingMatrices.get_input(1)
            transposeMatrix.to_transpose(firstMatrix,True)
            next_choice = input("Type y(yes) to execute program again.\nType anything else to exit. ")
            if next_choice == "y":
                main()
            elif next_choice == "n":
                raise SystemExit
            else:
                raise SystemExit
        
        # case when user chooses symmetry test function
        elif user_choice == "5":
            user_matrix = gettingMatrices.get_input(1)
            symmetryTest.symmetry_test(user_matrix)
            next_choice = input("Type y(yes) to execute program again.\nType anything else to exit. ")
            if next_choice == "y":
                main()
            elif next_choice == "n":
                raise SystemExit
            else:
                raise SystemExit
        
        # case when user chooses vector * matrix function
        elif user_choice == "6":
            user_vector = gettingVectors.get_input(1)
            user_matrix = gettingMatrices.get_input(1)
            same_dimension = gettingVectors.check_length(user_vector,user_matrix)
            multiplyVectorAndMartix.multiply(user_vector, user_matrix, same_dimension)
            next_choice = input("Type y(yes) to execute program again.\nType anything else to exit. ")
            if next_choice == "y":
                main()
            elif next_choice == "n":
                raise SystemExit
            else:
                raise SystemExit
        
        # case when user chooses dot product function
        elif user_choice == "7":
            inputs = gettingVectors.get_input(2)
            first_vector = inputs[0]
            second_vector = inputs[1]
            same_dimension = gettingVectors.check_length(first_vector,second_vector)
            vectorDotProduct.dot_product(first_vector,second_vector,same_dimension)
            next_choice = input("Type y(yes) to execute program again.\nType anything else to exit. ")
            if next_choice == "y":
                main()
            elif next_choice == "n":
                raise SystemExit
            else:
                raise SystemExit
        
        # case when user chooses weighted dot product function
        elif user_choice == "8":
            inputs = gettingVectors.get_input(2)
            first_vector = inputs[0]
            second_vector = inputs[1]
            same_dimension = gettingVectors.check_length(first_vector,second_vector)
            print("Enter the weight")
            weight = gettingVectors.get_input(1)
            same_dimension = gettingVectors.check_length(first_vector,weight)
            weightedDotProduct.weighted_dot_product(first_vector,second_vector,weight)
            next_choice = input("Type y(yes) to execute program again.\nType anything else to exit. ")
            if next_choice == "y":
                main()
            elif next_choice == "n":
                raise SystemExit
            else:
                raise SystemExit
            
        else:
            print("Invalid input. Try again.")
            main()
            
main()
