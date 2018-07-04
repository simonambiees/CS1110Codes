def weighted_dot_product(x,y,weight):
    result = 0.0
    for i in range(len(weight)):
        result += float(weight[i])*float(x[i])*float(y[i])
        
    print("The result is "+str(result))
