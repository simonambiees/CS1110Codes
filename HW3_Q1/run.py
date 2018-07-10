from Matrix import Matrix
from Vector import Vector
def main():
    print("Welcome to this program.\nThis program can do several calculations with matrices and vectors.\nChoose one to begin")
    print("Choose [1] if you would like to perform a matrix addition")
    print("Choose [2] if you would like to perform a matrix subtraction")
    print("Choose [3] if you would like to perform a matrix multiplication")
    print("The two matrices should be of the same dimension!!!\n")
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
            matrix_one = Matrix()
            matrix_one.set_matrix()
            matrix_two = Matrix()
            matrix_two.set_matrix()
            matrix_one.add_to(matrix_two)
            next_choice = input("Type anything to exit. ")
            raise SystemExit
    
        # case when user chooses subtraction function
        elif user_choice == "2":
            matrix_one = Matrix()
            matrix_one.set_matrix()
            matrix_two = Matrix()
            matrix_two.set_matrix()
            matrix_one.minus(matrix_two)
            next_choice = input("Type anything to exit. ")
            raise SystemExit
    
        # case when user chooses multiply function
        elif user_choice == "3":
            matrix_one = Matrix()
            matrix_one.set_matrix()
            matrix_two = Matrix()
            matrix_two.set_matrix()
            matrix_one.multiply_by(matrix_two)
            next_choice = input("Type anything to exit. ")
            raise SystemExit
        
        # case when user chooses transpose function
        elif user_choice == "4":
            matrix_one = Matrix()
            matrix_one.set_matrix()
            matrix_one.to_transpose(True)
            next_choice = input("Type anything to exit. ")
            raise SystemExit
        
        # case when user chooses symmetry test function
        elif user_choice == "5":
            matrix_one = Matrix()
            matrix_one.set_matrix()
            matrix_one.is_symmetric()
            next_choice = input("Type anything to exit. ")
            raise SystemExit
        
        # case when user chooses vector * matrix function
        elif user_choice == "6":
            vector_one = Vector()
            vector_one.set_vector()
            matrix_one = Matrix()
            matrix_one.set_matrix()
            vector_one.multiply_to_matrix(matrix_one)
            next_choice = input("Type anything to exit. ")
            raise SystemExit
        
        # case when user chooses dot product function
        elif user_choice == "7":
            vector_one = Vector()
            vector_one.set_vector()
            vector_two = Vector()
            vector_two.set_vector()
            vector_one.dot_product(vector_two)
            next_choice = input("Type anything to exit. ")
            raise SystemExit
        
        # case when user chooses weighted dot product function
        elif user_choice == "8":
            vector_one = Vector()
            vector_one.set_vector()
            vector_two = Vector()
            vector_two.set_vector()
            weight = Vector()
            print("Next input the weight as a vector.")
            weight.set_vector()
            vector_one.weighted_dot(vector_two,weight)
            next_choice = input("Type anything to exit. ")
            raise SystemExit
            
        else:
            print("Invalid input. Try again.")
            main()
            
main()