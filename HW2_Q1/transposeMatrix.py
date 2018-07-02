def to_transpose(x):
    xt = [[]*len(x)]*len(x[0])
    
    
    

    
    for i in range(0,len(x)):
        for j in range(0,len(x[i])):
            for k in range(0,len(x[i])):
                xt[k].append(x[i][j])
    # print("\n\nThis is the transpose:")
    # for i in range(0, len(xt)):
    #     for j in range(0, len(xt[i])):
    #         print(str(xt[i][j]), end = " ") 
    #     print("\n")
    print(xt)
    return xt