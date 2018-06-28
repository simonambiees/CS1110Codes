def add(x,y):
    result = []
    tempRowResult = []
    for i in range(0,len(x)-1):
        for j in range(0,len(x[i])-1):
            tempRowResult.append(float(x[i][j])+float(y[i][j]))
            result.append(tempRowResult)

    return result