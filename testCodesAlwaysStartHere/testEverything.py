import numpy as np


def get_a_matrix():
    matrix = []
    row_num = 1
    while True:
        row = input("row {}:".format(row_num))
        if row:
            matrix.append(list(map(int, row.split())))
            row_num += 1
        else:
            break

    return matrix


def get_two_np_matrix():
    print("Please input matrix(vector) 1")
    matrix1 = np.array(get_a_matrix())
    print("Please input matrix(vector) 2")
    matrix2 = np.array(get_a_matrix())
    return matrix1, matrix2


def addition():
    print(np.add(*get_two_np_matrix()))


def subtraction():
    print(np.subtract(*get_two_np_matrix()))


def multiplication():
    print(np.multiply(*get_two_np_matrix()))


def transpose():
    print(np.array(get_a_matrix()).transpose())


def symmetric():
    raw_matrix = np.array(get_a_matrix())
    if np.array_equal(raw_matrix,raw_matrix.transpose()):
        print("This matrix is symmetrical")
    else:
        print("This matrix is asymmetrical")


def dot_product():
    print(np.dot(*get_two_np_matrix()))


def weighted_dot_product():
    print("Enter weight")
    weight = get_a_matrix()

    print("Enter vector 1")
    v1 = get_a_matrix()

    print("Enter vector 2")
    v2 = get_a_matrix()

    result = 0

    for n in range(len(weight)):
        result += weight[n][0] * v1[n][0] * v2[n][0]
    print(result)


def get_user_input():
    while True:
        print("Matrix calculator")
        print("""
        1> Addition
        2> Subtraction
        3> Multiplication (including vector)
        4> Calculating Transpose
        5> Symmetric testing
        6> Dot product
        7> Weighted dot product
        8> Quit
        """)

        choice = input("Your choice:")

        try:
            num = int(choice)
            if num == 1:
                addition()

            elif num == 2:
                subtraction()

            elif num == 3:
                multiplication()

            elif num == 4:
                transpose()

            elif num == 5:
                symmetric()
            elif num == 6:
                dot_product()

            elif num == 7:
                weighted_dot_product()

            elif num == 8:
                break

            else:
                print("No such option")
                continue

        except ValueError as e:
            print(e)
            print("Check your input")
            continue


def main():
    get_user_input()


if __name__ == '__main__':
    main()
