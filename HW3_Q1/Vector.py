from Matrix import Matrix
class Vector:
    def __init__(self):
        self.body = []
    def set_vector(self):
        user_input = input("Enter a vector. Example: x y z\n\n")
        self.body = user_input.split()
        if self.idiot_proof_digit(self.body) == False:
            print("input contains non-number characters. Enter to Exit.")
            x = input()
            raise SystemExit

    def multiply_to_matrix(self, a_matrix):
        if len(self.body) != len(a_matrix.rows_and_cols[0]):
            print("Not of proper dimension. Enter to exit.")
            x = input()
            raise SystemExit

        # calculating and storing the results
        result = []
        for i in range(0, len(a_matrix.rows_and_cols)):
            temp_result = 0.0
            for j in range(0,len(self.body)):
                temp_result += float(self.body[j])*float(a_matrix.rows_and_cols[i][j])
            result.append(temp_result)

        
        # printing the results
        for i in result:
            print("%.2f" % i+"|")
        return result

    # idiot proof for non-number inputs
    def idiot_proof_digit(self,x):
        check = True
        for i in x:
            try:
                float(i)
            except ValueError:
                check = False
        return check

    def dot_product(self, a_vector):
        if len(self.body) != len(a_vector.body):
            print("Not of proper dimension. Enter to exit.")
            x = input()
            raise SystemExit
        # calculating and storing the results
        result = 0.0
        for i in range(0, len(self.body)):
            result += float(self.body[i])*float(a_vector.body[i])
        # printing the results
        print("%.2f" % result)

    def weighted_dot(self, a_vector, weight):
        if len(self.body) != len(a_vector.body):
            print("Not of proper dimension. Enter to exit.")
            x = input()
            raise SystemExit
        elif len(self.body) != len(weight.body):
            print("Not of proper dimension. Enter to exit.")
            x = input()
            raise SystemExit
        elif len(a_vector.body) != len(weight.body):
            print("Not of proper dimension. Enter to exit.")
            x = input()
            raise SystemExit
        # calculating and storing the results
        result = 0.0
        for i in range(0, len(self.body)):
            result += float(self.body[i])*float(a_vector.body[i])*float(weight.body[i])
        # printing the results
        print("%.2f" % result)