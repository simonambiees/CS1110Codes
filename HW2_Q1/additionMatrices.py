def addition_matrix(x,y):
    result = []
    tempRowResult = []
    for i in range(0,len(x)):
        for j in range(0,len(x[i])):
            tempRowResult.append(float(x[i][j])+float(y[i][j]))
        result.append(tempRowResult)

    return result