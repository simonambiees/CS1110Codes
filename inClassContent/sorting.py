'''
Created on Jul 16, 2013
    To demo some python sorting algorithms
        @author: bailey
'''
def print_list(my_list):
    temp = ''
    for i in my_list :
        temp += str(i) + ", "
    print(temp)
    
def selection_sort(my_list):
    ''' to take a list and return a sorted version'''
    if len(my_list) == 0 : 
        return my_list
    n = len(my_list)
    for i in range(n-1) :
        minnie = my_list[i]
        minloc = i
        for j in range(i+1,n) :
            if my_list[j] < minnie :
                minnie = my_list[j]
                minloc = j
        my_list[minloc] = my_list[i]
        my_list[i] = minnie
    return my_list

def bubble_sort(my_list):
    ''' to take a list and return a sorted version'''
    if len(my_list) == 0 : 
        return my_list
    n = len(my_list)
    for i in range(n-1) :
        for j in range(i+1,n) :
            k = n - j + i # so k will run from n to n-(n-1)+i = i+1
            if my_list[k] < my_list[k-1] : # so smaller that value on left
                temp = my_list[k]          # then swap the two values
                my_list[k] = my_list[k-1]
                my_list[k-1] = temp
    return my_list
    
def bucket_sort(my_list):
    ''' assuming my_list to be a list of integers'''
    if len(my_list) == 0 : 
        return my_list
    big = my_list[0] # starting to find the extreme values
    small = my_list[0]
    for term in my_list : # to establish max range of possible values
        if term > max :
            big = term
        if term < min :
            small = term
    freq = [ ] # to hold frequencies for values
    for i in range(small, big + 1) :
        freq.append(0) # initialising freqs to be zero
    for term in my_list :
        freq[term - min] += 1 # incrementing freqs
    i = 0
    for loc in range(len(freq)) : # run through freq list
        count = freq[loc]         # get frequency of occurrence to see how often to repeat value
        for more in range(count) : # repeat the insertion of the value _count_ times
            my_list[i] = loc + small
            i += 1
    return my_list
   
def merge_sort(my_list): 
    ''' a clear but space-inefficient implementation'''
    if len(my_list) == 0: # annoying silly case
        return my_list
    if len(my_list) == 1: # ·   base stopping case
        return my_list
    # so at this point my_list has length >= 2
    L_size = len(my_list) // 2 # note use of integer division
    R_size = len(my_list) - L_size 
    L_list = [ ]
    R_list = [ ]
    for i in range(L_size) : # build L_list to hold the left half of my_list
        L_list.append(my_list[i])
    for i in range(R_size) : # build R_list to hold the right half of my_list
        R_list.append(my_list[i+L_size])
    return merge( merge_sort(L_list) , merge_sort(R_list) ) # here we call the merge method to merge the sorted L and R lists

def merge(list_a, list_b): # to merge two lists where each is presumed to be sorted small to large
    combined = [ ]
    L_size = len(list_a)
    R_size = len(list_b)
    if L_size == 0 : # if both lists are empty, then returning either is equally good
        return list_b # if L_list is empty, simply return the R_list
    if R_size == 0 :
        return list_a # if R_list is empty, simply return the L_list
    a = 0 # to iterate along list_a
    b = 0 # to iterate along list_b
    while a < L_size and b < R_size : # while a and b are pointing _inside_ each list
        if list_a[a] < list_b[b] :
            combined.append(list_a[a])
            a += 1 # get ready to look at the next term in list_a
        else :
            combined.append(list_b[b])
            b += 1 # get ready to look at the next term in list_b
    if a < L_size : # so list_b is done but there's still more of list_a to go
        for the_rest in range(a, L_size) :
            combined.append(list_a[the_rest])
    if b < R_size : # so list_a is done but there's still more of list_b to go
        for the_rest in range(b, R_size) :
            combined.append(list_b[the_rest])
    return combined

def radix_sort(my_list):
    ''' assuming my_list to be a list of integers, and we'll proceed base 10 for clarity
        This could be vastly more efficient, but I've written the code to be highly transparent'''
    if len(my_list) == 0 : 
        return my_list
    shifted_list = [ ] # to hold the values once shifted by the smallest value
    big = my_list[0] # starting to find the extreme values
    small = my_list[0]
    for term in my_list : # to establish max range of possible values
        if term > big :
            big = term
        if term < small :
            small = term
    spread = big - small # the max range of numbers
    for value in my_list :
        shifted_list.append(value - small) # so sorting a list whose smallest is zero
    print (shifted_list)
    base = 10
    radix = get_radix(spread, base)
    print("radix = " + str(radix))
    digitised = [] # to hold the digitised values of my_list relative to the base
    for value in shifted_list :
        digitised.append(long_get_digits(value, radix, base))
    print(digitised)
    buckets = [ ] # to hold the various queues of values
    for count in range(base) : # one bucket for each potential value of a 'digit'
        buckets.append(Queuer(count))
    for k in range(radix) :
        for value in digitised :
            buckets[value[radix - k - 1]].insert(value)
        for b in buckets : print(b)
        digitised = [ ] # empty and re-use
        for q in buckets :
            while not q.isEmpty() :
                digitised.append(q.leave())
        print(digitised)
    my_list = [ ] # re-use this list
    for digital in digitised :
        my_list.append(reform_number(digital) + small) # so 'unshifting' the values back
    return my_list

def get_radix(spread, base=10): # default base is 10
    ''' assume spread > 0 and base > 1'''
    n = 1 # to explore the least power of base to exceed spread
    temp = base
    while spread >= temp :
        temp *= base
        n += 1 # to try the next power of base
    return n

def get_digits(value, base=10):
    radix = get_radix(value, base)
    digits = [ ] # to hold the digits of spread relative to the value of base
    for count in range(radix) :
        digits.append(value % base)
        value = value // base
    digits.reverse() # for human sanity!!
    return digits

def long_get_digits(value, radix, base=10):
    ''' to fill in with leading zeros as needed'''
    digits = get_digits(value, base)
    digits.reverse() # easy trick to prepend the right number of zeros
    n = len(digits)
    for count in range(radix - n) :
        digits.append(0)
    digits.reverse()
    return digits
    
def reform_number(digital, base=10):
    ''' assuming digital is a list of digits to that base'''
    radix = len(digital)
    temp_power = base
    temp = digital[radix - 1]
    for k in range(1, radix) :
        temp += digital[radix - k - 1] * temp_power
        temp_power *= base
    return temp

class Queuer :
    def __init__(self, name):
        self.front = None
        self.back = None
        self.length = 0
        self.name = name
        
    def __str__(self):
        if self.isEmpty() :
            return str(self.name) + ' queue is empty'
        iterator = self.front
        temp = str(self.name) + "-queue = " + str(iterator.getData()) + ", "
        while not iterator.getNext() is None :
            iterator = iterator.getNext()
            temp += str(iterator.getData()) + ", "
        return temp
    
    def insert(self, thing):
        if self.isEmpty() :
            self.front = Q_Node(thing)
            self.back = self.front
            self.length = 1
        else :
            self.back.setNext( Q_Node(thing) )
            self.back = self.back.getNext()
            self.length += 1
            
    def leave(self):
        if self.isEmpty() :
            return None
        else :
            temp = self.front.getData()
            self.front = self.front.getNext()
            self.length -= 1
            return temp
            
    def isEmpty(self):
        return self.length == 0
    
class Q_Node :
    def __init__(self, data=None, my_next=None):
        self.data = data
        self.my_next = my_next
        
    def __str__(self):
        return str(self.data)
    
    def setData(self, data):
        self.data - data
    def setNext(self, my_next):
        self.my_next = my_next
    def getData(self):
        return self.data
    def getNext(self):
        return self.my_next




#ugly_list = [96,16,12,3,5,24,8,2,17,31,23,4,18,6,3,19,16,3,17,99,4,3,55,12,3,8,9,-7,-98,77]
ugly_list = [14,39,22, 78, 99,42,11,31,76,17,83]

print_list(ugly_list)
nice_list = radix_sort(ugly_list)

print("\tAfter sorting, this is ...")
print_list(nice_list)
'''
q = Queuer(999)
q.insert("alan")
q.insert("beth")
q.insert("carol")
q.insert("dave")
print(q)
q.leave()
q.leave()
q.leave()
q.leave()
q.insert("weoriu")
print(q)
'''
