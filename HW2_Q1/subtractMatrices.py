def subtract_matrix(x,y,check):
    if check:
        result = []
        
        for i in range(0,len(x)):
            tempRowResult = []
            for j in range(0,len(x[i])):
                tempRowResult.append(float(x[i][j])-float(y[i][j]))
            result.append(tempRowResult)
        print("\n\nThis is the result:")
        for i in range(0, len(result)):
            for j in range(0, len(result[i])):
                print(str(result[i][j]), end = " ") 
            print("")
            
    else:
        result = "Not of the same dimension. Cannot subtract."
        print(result)
    