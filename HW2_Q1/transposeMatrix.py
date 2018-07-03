def to_transpose(x,y):
    height = len(x)
    width = len(x[0])
    xt = []
    for i in range(0, width): 
        temp = []   
        for j in range(0, height):
            temp.append(x[j][i])
        xt.append(temp)
    if y:
        for i in range(0, len(xt)):
            for j in range(0, len(xt[i])):
                print(str(xt[i][j]), end = " ") 
            print("")
    return xt