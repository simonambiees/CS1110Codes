from gettingMatrices import *
from additionMatrices import *

firstMatrix = get_first_input()
secondMatrix = get_second_input()
result = addition_matrix(firstMatrix,secondMatrix)

for i in range(0, len(result)):
    for j in range(0, len(result[i])):
        print(str(result[i][j]), end = " ") 
    print("")

