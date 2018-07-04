def multiply(x, y, check):
    result = []
    for i in range(0, len(y)):
        temp_result = 0.0
        for j in range(0,len(x)):
            temp_result += float(x[j])*float(y[i][j])
        result.append(temp_result)
    for i in result:
        print(str(i) + "\n")
    return result  

