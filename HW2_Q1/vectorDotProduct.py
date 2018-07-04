import Menu
def dot_product(x, y, check):
    if not check:
        print("Not of proper dimensions. Try again.")
        Menu.jump()
    result = 0.0
    for i in range(0, len(x)):
        result += float(x[i])*float(y[i])
    print("%.2f" % result)
