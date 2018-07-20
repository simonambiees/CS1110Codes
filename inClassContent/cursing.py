def factorial(number):
    if number >= 1:
        return number * factorial(number - 1)
    if number == 0:
        return 1
    print("I can't cope with negative numbers")
    return 0  ## silly answer

def helpFib(number):
    store = []
    store.append(1) # sets the 0-th Fibonacci value to 1
    store.append(1) # sets the 1-th Fibonacci value to 1
    for loc in range(2, number + 1) : # so we'll find a_(number - 1) as the (number)-th Fibonacci no.
        store.append(None) # or any other silly number
    return fibby(number, store) # we'll use store as our memory of previously computed values

def fibby(n, s): # n is a number and s is the store
    if s[n] != None : ### ie, we've calculated this value already, so don't recalculate it!!!
        return s[n]
    else :
        s[n] = fibby(n-1, s) + fibby(n-2, s)
        return s[n]
    print("I can't cope with negative numbers")
    return -999  ## silly answer


### the calling program
print("Calculating factorials, etc.")
n = 100

fib = helpFib(n)
print("The "+str(n+1)+ "-th Fibonacci is .... " +str(fib))

