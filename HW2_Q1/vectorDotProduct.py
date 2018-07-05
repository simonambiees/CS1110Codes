import main
def dot_product(x, y, check):
    # check if input of proper dimensions
    if not check:
        print("Not of proper dimensions. Try again.")
        main.main()
    # calculating and storing the results
    result = 0.0
    for i in range(0, len(x)):
        result += float(x[i])*float(y[i])
    # printing the results
    print("%.2f" % result)
