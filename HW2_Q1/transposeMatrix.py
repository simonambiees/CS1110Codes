def to_transpose(x:"List, containing the matrix",y:"Boolean, whether wants printed output"):
    # getting the row and col numbers of the matrix
    height = len(x)
    width = len(x[0])
    
    # initializing a list for storing the result
    xt = []
    
    # storing the result
    for i in range(0, width): 
        temp = []   
        for j in range(0, height):
            temp.append(x[j][i])
        xt.append(temp)
    
    # checking if user wants output to console
    if y:
        # printing the result in a formatted way
        for i in range(0, len(xt)):
            for j in range(0, len(xt[i])):
                print(str(xt[i][j]), end = "|") 
            print("")
    return xt
