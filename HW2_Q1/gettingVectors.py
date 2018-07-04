import idiotProof
import Menu

def get_input(x:"Int: how many vectors are needed"):
    
    # case when only one vector is needed as input
    if x == 1:
        user_input = input("Enter a vector. Example: x y z\n")
        user_vector = user_input.split()
        if idiotProof.idiot_proof_digit(user_vector) == False:
            print("input contains non-number characters. Try again.")
            Menu.jump()
        return user_vector
        
    # case when two vectors are needed as inputs
    elif x == 2:
        first_user_input = input("Enter the first vector. Example: x y z\n")
        first_user_vector = first_user_input.split()
        if idiotProof.idiot_proof_digit(first_user_vector) == False:
            print("input contains non-number characters. Try again.")
            Menu.jump()
        

        second_user_input = input("Enter the second vector. Example: x y z\n")
        second_user_vector = second_user_input.split()
        if idiotProof.idiot_proof_digit(second_user_vector) == False:
            print("input contains non-number characters. Try again.")
            Menu.jump()
        
        two_vectors = []
        two_vectors.append(first_user_vector)
        two_vectors.append(second_user_vector)
        return two_vectors

def check_length(x, y):
    check = True
    if len(x) != len(y):
        check = False
    return check

