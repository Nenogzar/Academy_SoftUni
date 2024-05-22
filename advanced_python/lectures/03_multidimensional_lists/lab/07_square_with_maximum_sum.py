#################################### TASK CONDITION ############################
"""
                    7.	Square with Maximum Sum
Write a program that reads a matrix from the console and finds the 2x2 top-left 
submatrix with biggest sum of its values. On first line you will get matrix 
sizes in format "{rows}, {columns}".  On the next rows, you will get elements 
for each column, separated with a comma and a space ", ".  You should print 
the found submatrix and the sum of its elements, as shown in the examples. 

____________________________________________________________________________________________
Example_01

Input
3, 6
7, 1, 3, 3, 2, 1
1, 3, 9, 8, 5, 6
4, 6, 7, 9, 1, 0	

Output
9 8
7 9
33

____________________________________________________________________________________________
Example_02

Input
2, 4
10, 11, 12, 13
14, 15, 16, 17

Output
12 13 
16 17 
58

Hints
•	Be aware of IndexError
•	If you find more than one max square, print the top-left one

"""

##########: variant 1 :##########

rows, cols = list(map(int, input().split(", ")))

matrix = []
for i in range(rows):
    row = list(map(int, input().split(", ")))
    matrix.append(row)

max_sum = -float('inf')
max_matrix = []
for i in range(rows - 1):
    for j in range(cols - 1):
        sub_matrix = [
            [matrix[i][j], matrix[i][j + 1]],
            [matrix[i + 1][j], matrix[i + 1][j + 1]]
        ]
        current_sum = 0
        for row in sub_matrix:
            current_sum += sum(row)
        if current_sum > max_sum:
            max_sum = current_sum
            max_matrix = sub_matrix

for r in max_matrix:
    print(*r, sep=" ")
print(max_sum)



    ##########: variant 2 :##########

rows, colons = list(map(int, input().split(", ")))
 
matrix_list = [list(map(int, input().split(", "))) for _ in range(rows)]
max_sum = {"max number": float('-inf'), "row": 0, "col": 0}
 
def check_valid_index(row, col):
    return row + 1 < rows and col + 1 < colons
 
def sum_square(row, col):
    if check_valid_index(row, col):
        sum_total = matrix_list[row][col] + matrix_list[row][col + 1] + matrix_list[row + 1][col] + matrix_list[row + 1][col + 1]
        if max_sum["max number"] < sum_total:
            max_sum["max number"] = sum_total
            max_sum["row"] = row
            max_sum["col"] = col
 
for row in range(rows):
    for col in range(colons):
        sum_square(row, col)
 
for row in range(max_sum["row"], max_sum["row"] + 2):
    print(" ".join(map(str, matrix_list[row][max_sum["col"]: max_sum["col"] + 2])))
print(max_sum['max number'])


    ##########: variant 3 - Class :##########
class MaxSumSquare:

    def __init__(self):
        self.result_message = ''
        self.rows = 0
        self.cols = 0
        self.matrix = []
        self.square = []
        self.square_sum = 0
        self.main_meth()

    def main_meth(self):
        self.define_rows_and_cols_for_matrix()
        self.create_matrix()
        self.search_in_matrix_biggest_square_sum()
        self.prepare_result()

    def define_rows_and_cols_for_matrix(self):
        self.rows, self.cols = [int(x) for x in input().split(', ')]

    def create_matrix(self):
        for _ in range(self.rows):
            row = [int(num) for num in input().split(', ')]
            self.matrix.append(row)

    def search_in_matrix_biggest_square_sum(self):
        for row in range(self.rows - 1):
            for col in range(self.cols - 1):
                sum_of_square = self.sum_numbers_in_square(row, col)
                self.check_square_sum(sum_of_square, row, col)

    def sum_numbers_in_square(self, row, col):
        sum_of_numbers = self.matrix[row][col] + self.matrix[row][col + 1] + \
                         self.matrix[row + 1][col] + self.matrix[row + 1][col + 1]
        return sum_of_numbers

    def check_square_sum(self, some_sum, row, col):
        if some_sum > self.square_sum:
            self.square_sum = some_sum
            self.square = [[self.matrix[row][col], self.matrix[row][col + 1]],
                           [self.matrix[row + 1][col], self.matrix[row + 1][col + 1]]]

    def prepare_result(self):
        self.result_message = "\n".join(' '.join(str(x) for x in row) for row in self.square)
        self.result_message += f"\n{self.square_sum}"

    def __repr__(self):
        return self.result_message


if __name__ == '__main__':
    print(MaxSumSquare())


