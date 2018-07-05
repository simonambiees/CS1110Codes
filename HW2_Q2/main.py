import idiotProof
import time

def getting_pos():
    # Asking for user input of matrix
    blank_check = input("Enter pairs of x_pos and y_pos.\nExample: x y\nKeep entering until you do not want any more\n\n")
    # Interpreting the user input
    new_pos = blank_check.split()
    if idiotProof.idiot_proof_digit(new_pos) == False:
        print("Illegal characters entered. Program cannot execute.\nHowever, as the mighty Thor, son of Odin, I give you a second chance!")
        run_program()     
        # initializing a list for containing user input
    row_and_col = []
    row_and_col.append(new_pos)

    # start of loop for checking if the user wants to end typing and storing inputs into a list.
    while len(blank_check) != 0:
        blank_check = input()
        new_row = blank_check.split()
        row_and_col.append(new_row)
        # idiot proof code in case non-number characters & wrong matrices are entered
        if idiotProof.idiot_proof_digit(new_row) == False:
            print("Illegal characters entered. Program cannot execute.")
            raise SystemExit
        elif idiotProof.idiot_proof_dimension(row_and_col) == False:
            print("Not a matrix. Program cannot execute.")
            raise SystemExit
    # deleting the last empty element to avoid error when parsing str into float
    row_and_col.pop(len(row_and_col)-1)
    return row_and_col
    
def getting_constants():
    constants_input = [0.0,0.0]
    constant_a = input("Please enter the constant_a_ in y=ax+b.\nEntering nothing/non-number means use (0.0,0.0)\n")
    constant_b = input("Please enter the constant_b_ in y=ax+b.\n")
    try:
        constants_input[0] = float(constant_a)
    except:
        print("Using default values a=0.0\n")
    try:
        constants_input[1] = float(constant_b)
        return constants_input
    except:
        print("Using default values b=0.0\n\n\n")
        return constants_input

def the_line(a,b,x):
    y = float(x)*a+b
    return y
    
def compare_y_pos(a,b,points):
    
    result_above = []
    result_on = []
    result_below = []
    for i in points:
        if float(i[1])>the_line(a,b,i[0]):
            temp = i
            result_above.append(temp)
        elif float(i[1])==the_line(a,b,i[0]):
            temp = i
            result_on.append(temp)
        elif float(i[1])<the_line(a,b,i[0]):
            temp = i
            result_below.append(temp)
        else:
            print("Invalid values entered.")
    print("Points above the line:")
    print(result_above)
    print("Points on the line:")
    print(result_on)
    print("Points below the line:")
    print(result_below)
    above = ""
    on = ""
    below = ""
    file = open("HW2_Q2\\ProgramResults.txt","w")
    localtime = time.asctime(time.localtime(time.time()))
    file.writelines(localtime)
    file.writelines("\n")
    file.writelines("Line: y=%.1fx+%.1f" % (a,b))
    file.writelines("\n")
    file.writelines("Above the line:")
    file.writelines("\n")
    for i in result_above:
        above += (str(i[0])+","+str(i[1])+"|")
    file.writelines(above)
    file.writelines("\n")
    file.writelines("On the line:")
    file.writelines("\n")
    for i in result_on:
        on += (str(i[0])+","+str(i[1])+"|")
    file.writelines(on)
    file.writelines("\n")
    for i in result_below:
        below += (str(i[0])+","+str(i[1])+"|")
    file.writelines("Below the line:")
    file.writelines("\n")
    file.writelines(below)
    file.writelines("\n")
    file.writelines("_______________________________________________________________________________________________________________")
    file.writelines("\n")
    file.close()
    user_choice = input("Enter y to execute again. Enter anything else to exit and see the results in file \"ProgramResults.txt\"")
    if user_choice == "y":
        run_program()
    elif user_choice == "n":
        raise SystemExit
    else:
        raise SystemExit
        
def run_program():
    points = getting_pos()
    print(points)
    constants = getting_constants()
    compare_y_pos(float(constants[0]),float(constants[1]),points)
    
run_program()

    


