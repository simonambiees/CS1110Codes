def getting_pos():
    pos_input = [0.0,0.0]
    x_pos = input("Please enter the x-coordinate of the point you want to investigate.\nEntering nothing/non-number means use (0.0,0.0)\n")
    y_pos = input("Please enter the y-coordinate of the point you want to investigate.\n")
    try:
        pos_input[0] = float(x_pos)
        pos_input[1] = float(y_pos)
        return pos_input
    except:
        print("Using default values x_pos=0.0 and y_pos=0.0")
        return pos_input
    
def getting_constants():
    constants_input = [0.0,0.0]
    constant_a = input("Please enter the constant_a_ in y=ax+b.\nEntering nothing/non-number means use (0.0,0.0)\n")
    constant_b = input("Please enter the constant_b_ in y=ax+b.\n")
    try:
        constants_input[0] = float(constant_a)
        constants_input[1] = float(constant_b)
        return constants_input
    except:
        print("Using default values a=0.0 and b=0.0\n\n\n")
        return constants_input

def the_line(a,b,x):
    y = x*a+b
    return y
    
def compare_y_pos(y_line,y_point):
    if y_point>y_line:
        print("The point is above the line.")
    elif y_point==y_line:
        print("The point is on the line.")
    elif y_point<y_line:
        print("The point in below the line.")
    else:
        print("Invalid values entered.")

try:
    pos = getting_pos()
    constants = getting_constants()
    compare_y_pos(the_line(constants[0],constants[1],pos[0]),pos[1])
except:
    print("")
