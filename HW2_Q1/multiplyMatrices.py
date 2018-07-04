def multi_matrix(x:"List, first matrix",y:"List, second matrix",check:"Boolean: if the matrices have appropriate dimensions"):
    if check:
        result = []
        
        # for loop for getting the cooresponding values from the two matrices being multiplied together and multiplying them
        for i in range(0,len(x)):
            temp = []
            for j in range(0, len(y[i])):
                single_result = 0.0
                for k in range(0, len(y)):
                    single_result += float(x[i][k])*float(y[k][j])
                temp.append(single_result)
            # stores the calculated values to a list for storage and presentation
            result.append(temp)
        # printing out the results in a formatted way for the user to see
        print("\n\nThis is the result:")
        for i in range(0, len(result)):
            for j in range(0, len(result[i])):
                print("%.4f" % result[i][j], end = "|") 
            print("")
    else:
        # output in case the two matrices cannot be multiplied
        result = "Not of proper dimensions. Cannot multiply."
        print(result)
