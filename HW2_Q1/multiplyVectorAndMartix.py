import main
def multiply(x, y, check):
    # check if input of correct dimensions
    if not check:
        print("Not of proper dimension. Try again.")
        main.main()\
    # calculating and storing the results
    result = []
    for i in range(0, len(y)):
        temp_result = 0.0
        for j in range(0,len(x)):
            temp_result += float(x[j])*float(y[i][j])
        result.append(temp_result)

    # printing the results
    for i in result:
        print("%.2f" % i + "\n")
    return result  

