def idiot_proof_digit(x:"List, containing strings to be checked if has all numbers"):
    check = True
    for i in x:
        if i.isdigit() == False:
            check = False
    return check

def idiot_proof_dimension(x:"List, containing lists that make up a matrix"):
    check = True
    for i in range(1, len(x)):
        if len(x[i]) != len(x[i-1]):
            check = False
    return check
