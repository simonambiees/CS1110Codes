class Matrix:
    def __init__(self, rows, cols):
        ###takes in the number of rows and cols needed for the matrix###
        self.number_rows = rows
        self.number_cols = cols
        self.rows_and_cols = [[0]*cols for i in range(rows)]

    def get_matrix(self, matrix):
        print(self.rows_and_cols)

    def get_item(self, index_row, index_col):
        print(self.rows_and_cols[index_row][index_col])
