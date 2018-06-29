# This programs takes in a series of numbers that user inputs and sorts them to find max and min and mean

def get_first_input():
    # Asking for user input of first matrix
    first_blank_check = input("Enter the first row numbers. Separate with a space. Hit enter for next row.\n")
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
    return first_row_and_col

def get_second_input():
    # Asking for user input of second matrix
    second_blank_check = input("Enter the second row numbers. Separate with a space. Hit enter for net row.\n")
    #Interpreting the user input
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
    return second_row_and_col

def check_dimension(x, y):
    dimension_same = True
    if len(x) != len(y):
        dimension_same = False
    elif len(x) == len(y):
        if len(x[0]) != len(y[0]):
            dimension_same = False

    return dimension_same

