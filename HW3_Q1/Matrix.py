class Matrix:
    def __init__(self):
        ###takes in the number of rows and cols needed for the matrix###
        self.rows_and_cols = []
    
    # idiot proof in case incorrect matrices are input
    def idiot_proof_dimension(self,x:"List, containing lists that make up a matrix"):
        check = True
        for i in range(1, len(x)-1):
            if len(x[i]) != len(x[i-1]):
                check = False
        return check
    
    # idiot proof for non-number inputs
    def idiot_proof_digit(self,x:"List, containing strings to be checked if has all numbers"):
        check = True
        for i in x:
            try:
                float(i)
            except ValueError:
                check = False
        return check

    def get_matrix(self):
        print(self.rows_and_cols)

    def get_item(self, index_row, index_col):
        print(self.rows_and_cols[index_row][index_col])

    def set_matrix(self):
        blank_check = input("Input matrix.\nExample: 1 2 3\n         4 5 6\n         7 8 9\n\n")
        new_row = blank_check.split()
        if self.idiot_proof_digit(new_row) == False:
            print("Illegal characters entered. Program cannot execute. Enter to exit.")
            x = input()
            raise SystemExit
        self.rows_and_cols.append(new_row)

        # start of loop for checking if the user wants to end typing and storing inputs into a list.
        while len(blank_check) != 0:
            blank_check = input()
            new_row = blank_check.split()
            self.rows_and_cols.append(new_row)
            # idiot proof code in case non-number characters & wrong matrices are entered
            if self.idiot_proof_digit(new_row) == False:
                print("Illegal characters entered. Program cannot execute. Enter to exit.")
                x = input()
                raise SystemExit
            elif self.idiot_proof_dimension(self.rows_and_cols) == False:
                print("Not a matrix. Program cannot execute. Enter to exit.")
                x = input()
                raise SystemExit

        # deleting the last empty element to avoid error when parsing str into float
        self.rows_and_cols.pop(len(self.rows_and_cols)-1)

    def add_to(self, matrix_two):
        if len(self.rows_and_cols) != len(matrix_two.rows_and_cols):
            print("Two matrices not of same dimension. Enter to exit.")
            x = input()
            raise SystemExit
        elif len(self.rows_and_cols) == len(matrix_two.rows_and_cols):
            if len(self.rows_and_cols[0]) != len(matrix_two.rows_and_cols[0]):
                print("Two matrices not of same dimension. Enter to exit.")
                x = input()
                raise SystemExit
        
        result = []
        # for loop to process the two matrices entered to find thecooresponding values for addition
        for i in range(0,len(self.rows_and_cols)):
            tempRowResult = []
            for j in range(0,len(self.rows_and_cols[i])):
                tempRowResult.append(float(self.rows_and_cols[i][j])+float(matrix_two.rows_and_cols[i][j]))
            
            # storing the results in a list for storage and presentation
            result.append(tempRowResult)
        
        # printing out the result in a formatted way
        print("\n\nThis is the result:")
        for i in range(0, len(result)):
            for j in range(0, len(result[i])):
                print("%.2f" % result[i][j], end = "|") 
            print("")
    
    def minus(self, matrix_two):
        if len(self.rows_and_cols) != len(matrix_two.rows_and_cols):
            print("Two matrices not of same dimension. Enter to exit.")
            x = input()
            raise SystemExit
        elif len(self.rows_and_cols) == len(matrix_two.rows_and_cols):
            if len(self.rows_and_cols[0]) != len(matrix_two.rows_and_cols[0]):
                print("Two matrices not of same dimension. Enter to exit.")
                x = input()
                raise SystemExit
        
        result = []
        # for loop to process the two matrices entered to find thecooresponding values for subtraction
        for i in range(0,len(self.rows_and_cols)):
            tempRowResult = []
            for j in range(0,len(self.rows_and_cols[i])):
                tempRowResult.append(float(self.rows_and_cols[i][j])-float(matrix_two.rows_and_cols[i][j]))
            
            # storing the results in a list for storage and presentation
            result.append(tempRowResult)
        
        # printing out the result in a formatted way
        print("\n\nThis is the result:")
        for i in range(0, len(result)):
            for j in range(0, len(result[i])):
                print("%.2f" % result[i][j], end = "|") 
            print("")

    def to_transpose(self, print_or_not):
        # getting the row and col numbers of the matrix
        height = len(self.rows_and_cols)
        width = len(self.rows_and_cols[0])
    
        # initializing a list for storing the result
        xt = []
    
        # storing the result
        for i in range(0, width): 
            temp = []   
            for j in range(0, height):
                temp.append(self.rows_and_cols[j][i])
            xt.append(temp)
        # checking if user wants output to console
        if print_or_not:
            # printing the result in a formatted way
            for i in range(0, len(xt)):
                for j in range(0, len(xt[i])):
                    print(str(xt[i][j]), end = "|") 
                print("")
        return xt

    def multiply_by(self, matrix):
        matrix = matrix.to_transpose(False)
        if len(self.rows_and_cols) != len(matrix):
            print("Two matrices not of appropriate dimension. Enter to exit.")
            x = input()
            raise SystemExit
        result = []
        for i in range(0, len(matrix[0])):
            temp = []
            for j in range(0, len(self.rows_and_cols[0])):
                x = 0.0
                for k in range(0, len(self.rows_and_cols)):
                    x += (float(self.rows_and_cols[k][j])*float(matrix[k][i]))
                temp.append(x)
            result.append(temp)

        # printing out the result in a formatted way
        print("\n\nThis is the result:")
        for i in range(0, len(result)):
            for j in range(0, len(result[i])):
                print("%.2f" % result[i][j], end = "|") 
            print("")
    def is_symmetric(self):
        if self.to_transpose(False) == self.rows_and_cols:
            print("This matrix is symmetric.")
        else:
            print("This matrix is not symmetric.")