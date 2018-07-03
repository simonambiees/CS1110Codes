def addition_matrix(x:"List: first matrix to be added",y:"List: second list to be added",check:"Boolean, whether matrices are of same dimensions"):
    if check:
        result = []
        # for loop to process the two matrices entered to find thecooresponding values for addition
        for i in range(0,len(x)):
            tempRowResult = []
            for j in range(0,len(x[i])):
                tempRowResult.append(float(x[i][j])+float(y[i][j]))
            
            # storing the results in a list for storage and presentation
            result.append(tempRowResult)
        
        # printing out the result in a formatted way
        print("\n\nThis is the result:")
        for i in range(0, len(result)):
            for j in range(0, len(result[i])):
                print(str(result[i][j]), end = " ") 
            print("")
            
    else:
        # idiot proof codes in case inappropiate matrices are entered by user
        result = "Not of the same dimension. Cannot add."
        print(result)
    
