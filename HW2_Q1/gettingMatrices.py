# This programs takes in a series of numbers that user inputs and sorts them to find max and min and mean

def get_input(x:"Int: how many matrices are needed"):
    
    # case when only one matrix is needed as input
    if x == 1:
        # Asking for user input of matrix
        blank_check = input("Enter a matrix.\nExample: 1 2 3\n         4 5 6\n         7 8 9\n\n")
        # Interpreting the user input
        new_row = blank_check.split()
        # initializing a list for containing user input
        row_and_col = []
        row_and_col.append(new_row)

        # start of loop for checking if the user wants to end typing and storing inputs into a list.
        while len(blank_check) != 0:
            blank_check = input()
            new_row = blank_check.split()
            row_and_col.append(new_row)

        # deleting the last empty element to avoid error when parsing str into float
        row_and_col.pop(len(row_and_col)-1)
        return row_and_col
        
    # case when two matrices are needed as inputs
    elif x == 2:
        # Asking for user input of first matrix
        first_blank_check = input("Enter the first matrix. \nExample: 1 2 3\n         4 5 6\n         7 8 9\n")
        # Interpreting the user input
        first_new_row = first_blank_check.split()
        # initializing a list for containing user input
        first_row_and_col = []
        first_row_and_col.append(first_new_row)

        # start of loop for checking if the user wants to end typing and storing inputs into a list.
        while len(first_blank_check) != 0:
            first_blank_check = input()
            first_new_row = first_blank_check.split()
            first_row_and_col.append(first_new_row)

        # deleting the last empty element to avoid error when parsing str into float
        first_row_and_col.pop(len(first_row_and_col)-1)
        
        
        # Asking for user input of second matrix
        second_blank_check = input("Enter the second matrix. \nExample: 1 2 3\n         4 5 6\n         7 8 9\n")
        # Interpreting the user input
        second_new_row = second_blank_check.split()
        # initializing a list for containing user input
        second_row_and_col = []
        second_row_and_col.append(second_new_row)

        # start of loop for checking if the user wants to end typing and storing inputs into a list.
        while len(second_blank_check) != 0:
            second_blank_check = input()
            second_new_row = second_blank_check.split()
            second_row_and_col.append(second_new_row)

        # deleting the last empty element to avoid error when parsing str into float
        second_row_and_col.pop(len(second_row_and_col)-1)
        two_matrices = [first_row_and_col, second_row_and_col]
        return two_matrices
    

def check_dimension(x, y, z):
    if not z:
        dimension_same = True
        if len(x) != len(y):
            dimension_same = False
        elif len(x) == len(y):
            if len(x[0]) != len(y[0]):
                dimension_same = False
    elif z:
        dimension_same = True
        if len(x[0]) != len(y[0]):
            dimension_same = False

    return dimension_same

