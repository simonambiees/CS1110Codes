def weighted_dot_product(x,y,weight):
    # calculating and storing the results
    result = 0.0
    for i in range(len(weight)):
        result += float(weight[i])*float(x[i])*float(y[i])
    # printing the results
    print("The result is "+str(result))
