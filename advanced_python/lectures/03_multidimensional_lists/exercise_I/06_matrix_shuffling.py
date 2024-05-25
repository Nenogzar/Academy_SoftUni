#################################### TASK CONDITION ############################
"""
https://judge.softuni.org/Contests/Compete/Index/1835#5

                           6.	Matrix Shuffling
Write a program that reads a matrix from the console and performs certain 
operations with its elements. User input is provided similarly to the 
problems above - first, you read the dimensions and then the data.  Your 
program should receive commands in the format: "swap {row1} {col1} {row2} {col2}"
 where ("row1", "col1") and ("row2", "col2") are the coordinates of two points in 
 the matrix. A valid command starts with the "swap" keyword along with four 
 valid coordinates (no more, no less), separated by a single space.
•	If the command is valid, you should swap the values at the given indexes 
and print the matrix at each step (thus, you will be able to check if the 
operation was performed correctly). 
•	If the command is not valid (does not contain the keyword "swap", has fewer 
or more coordinates entered, or the given coordinates are not valid), 
print "Invalid input!" and move on to the following command. 
A negative value makes the coordinates not valid.
Your program should finish when the command "END" is entered.

____________________________________________________________________________________________
Example_01

Input
2 3
1 2 3
4 5 6
swap 0 0 1 1
swap 10 9 8 7
swap 0 1 1 0
END	

Output
5 2 3
4 1 6
Invalid input!
5 4 3
2 1 6

____________________________________________________________________________________________
Example_02

Input
1 2
Hello World
0 0 0 1
swap 0 0 0 1
swap 0 1 0 0
END	

Output
Invalid input!
World Hello
Hello World


"""


    ##########: variant 1 :##########


rows, cols = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for _ in range(rows)]
output_message = ''

while True:
    line = input().split()
    if line[0] == 'END':
        break

    command = line[0]
    indexes = [int(n) for n in line if n.isdigit()]

    if command == 'swap' and len(indexes) == 4:
        row1, col1, row2, col2 = indexes
        if 0 <= row1 < rows and 0 <= col1 < cols and 0 <= row2 < rows and 0 <= col2 < cols:
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            output_message += '\n'.join(' '.join(map(str, row)) for row in matrix) + '\n'
        else:
            output_message += 'Invalid input!\n'
    else:
        output_message += 'Invalid input!\n'

print(output_message)


    ##########: variant 2 : whit try - exept ##########



rows, cols = map(int, input().split())
matrix = [input().split() for _ in range(rows)]

valid_rows, valid_cols = range(rows), range(cols)

command = input().split()
while command[0] != "END":
    try:
        action, *coordinates = [int(x) if x.isdigit() else x for x in command]
    except ValueError:
        print("Invalid input!")
        command = input().split()
        continue

    if action == "swap" and len(coordinates) == 4:
        row1, col1, row2, col2 = coordinates
        if {row1, row2}.issubset(valid_rows) and {col1, col2}.issubset(valid_cols):
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            for row in matrix:
                print(*row)
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")

    command = input().split()



    ##########: variant 3 :##########



def indeces_is_valid(indeces):
    return {indeces[0], indeces[2]}.issubset(valid_rows) and {indeces[1], indeces[3]}.issubset(valid_cols)


def swap_elements(command, indeces):
    if len(indeces) == 4 and indeces_is_valid(indeces) and command == "swap":
        row1, col1, row2, col2 = indeces
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        [print(*row) for row in matrix]
    else:
        print("Invalid input!")


rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

valid_rows, valid_cols = range(rows), range(cols)

while True:
    command_type, *coordinates = [int(x) if x.isdigit() else x for x in input().split()]

    if command_type == 'END':
        break

    swap_elements(command_type, coordinates)


    ##########: variant 4 : whit try - exept ##########


def indeces_is_valid(indeces):
    return {indeces[0], indeces[2]}.issubset(valid_rows) and {indeces[1], indeces[3]}.issubset(valid_cols)

def swap_elements(command, indeces):
    if len(indeces) == 4 and indeces_is_valid(indeces) and command == "swap":
        row1, col1, row2, col2 = indeces
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        [print(*row) for row in matrix]
    else:
        print("Invalid input!")

rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

valid_rows, valid_cols = range(rows), range(cols)

while True:
    user_input = input().split()
    command_type = user_input[0]
    if command_type == 'END':
        break
    try:
        coordinates = list(map(int, user_input[1:]))
    except ValueError:
        print("Invalid input!")
        continue
    if command_type == 'swap' and len(coordinates) == 4:
        swap_elements(command_type, coordinates)
    else:
        print("Invalid input!")


    ##########: variant 4 - Class :##########

class ShuffleMatrix:

    def __init__(self):
        self.output_message = ''
        self.rows, self.cols = 0, 0
        self.matrix = []
        self.main_meth()

    def main_meth(self):
        self.define_rows_cols_for_matrix()
        self.fill_matrix_with_elements()
        self.start_to_shuffle_matrix()

    def define_rows_cols_for_matrix(self):
        self.rows, self.cols = [int(x) for x in input().split()]

    def fill_matrix_with_elements(self):
        self.matrix = [[x for x in input().split()] for _ in range(self.rows)]

    def start_to_shuffle_matrix(self):
        while True:
            line = input().split()
            if line[0] == 'END':
                break

            valid = self.validate_data(line)
            if valid:
                self.swap_elements(valid)
                self.output_message += '\n'.join(' '.join(map(str, row)) for row in self.matrix) + '\n'
            else:
                self.output_message += 'Invalid input!\n'

    def validate_data(self, data):
        command = data[0]
        indexes = [int(n) for n in data if n.isdigit()]
        if command == 'swap' and len(indexes) == 4:
            row1, col1, row2, col2 = indexes
            if 0 <= (row1 and row2) < self.rows and 0 <= (col1 and col2) < self.cols:
                return indexes

    def swap_elements(self, some_indexes):
        row1, col1, row2, col2 = [int(n) for n in some_indexes]
        self.matrix[row1][col1], self.matrix[row2][col2] = self.matrix[row2][col2], self.matrix[row1][col1]

    def __repr__(self):
        return self.output_message


if __name__ == '__main__':
    print(ShuffleMatrix())




    ##########: variant 5 - Class :##########


class ShuffleMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [input().split() for _ in range(rows)]
        self.valid_rows = range(rows)
        self.valid_cols = range(cols)

    def indeces_are_valid(self, indeces):
        return {indeces[0], indeces[2]}.issubset(self.valid_rows) and {indeces[1], indeces[3]}.issubset(self.valid_cols)

    def swap_elements(self, indeces):
        if len(indeces) == 4 and self.indeces_are_valid(indeces):
            row1, col1, row2, col2 = indeces
            self.matrix[row1][col1], self.matrix[row2][col2] = self.matrix[row2][col2], self.matrix[row1][col1]
            self.print_matrix()
        else:
            print("Invalid input!")

    def print_matrix(self):
        for row in self.matrix:
            print(*row)

    def process_commands(self):
        while True:
            command = input().split()
            if command[0] == "END":
                break
            try:
                action, *coordinates = [int(x) if x.isdigit() else x for x in command]
            except ValueError:
                print("Invalid input!")
                continue

            if action == "swap" and len(coordinates) == 4:
                self.swap_elements(coordinates)
            else:
                print("Invalid input!")


rows, cols = map(int, input().split())
shuffle_matrix = ShuffleMatrix(rows, cols)
shuffle_matrix.process_commands()
