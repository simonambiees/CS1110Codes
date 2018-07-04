def idiot_proof_digit(x:"List, containing strings to be checked if has all numbers"):
    for i in x:
        try:
            float(i)
            return True
        except ValueError:
            return False

def idiot_proof_dimension(x:"List, containing lists that make up a matrix"):
    check = True
    for i in range(1, len(x)-1):
        if len(x[i]) != len(x[i-1]):
            check = False
    return check
