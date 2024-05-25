#################################### TASK CONDITION ############################
"""
https://judge.softuni.org/Contests/Compete/Index/1835#1
                          1.	Diagonals
Using a nested list comprehension, write a program that reads rows of a square 
matrix and its elements, separated by a comma and a space ", ". You should find 
the matrix's diagonals, prints them and their sum in the format:
"Primary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_primary}

____________________________________________________________________________________________
Example

Input
3
1, 2, 3
4, 5, 6
7, 8, 9

Output
Primary diagonal: 1, 5, 9. Sum: 15
Secondary diagonal: 3, 5, 7. Sum: 15

"""

      ##########: variant 1 :##########
size = int(input())

matrix = []
for _ in range(size):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)

primary_diagonal = []
secondary_diagonal = []

for i in range(size):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[size - 1 - i][i])

primary_diagonal_str = ', '.join(str(x) for x in primary_diagonal)
secondary_diagonal_str = ', '.join(str(x) for x in reversed(secondary_diagonal))

output_message = f'Primary diagonal: {primary_diagonal_str}. Sum: {sum(primary_diagonal)}\n'
output_message += f'Secondary diagonal: {secondary_diagonal_str}. Sum: {sum(secondary_diagonal)}'


print(output_message)

      ##########: variant 2 :##########
n = int(input())
matrix = [[int(el) for el in input().split(", ")] for _ in range(n)]
# matrix = [list(map(int, input().split(", "))) for _ in range(n)]
primary = [matrix[i][i] for i in range(n)]
secondary = [matrix[i][n - i - 1] for i in range(n)]

print(f"Primary diagonal: {', '.join(str(x) for x in primary)}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary)} Sum: {sum(secondary)} ")


    ##########: variant 3 - Class :##########

class Diagonals:

    def __init__(self):
        self.output_message = ''
        self.size = int(input())
        self.matrix = []
        self.primary_diagonal = []
        self.secondary_diagonal = []
        self.main_meth()

    def main_meth(self):
        self.create_matrix()
        self.find_diagonals_of_matrix()
        self.prepare_output_message()

    def create_matrix(self):
        self.matrix = [[int(x) for x in input().split(', ')] for row in range(self.size)]

    def find_diagonals_of_matrix(self):
        for i in range(self.size):
            self.primary_diagonal.append(self.matrix[i][i])
            self.secondary_diagonal.append(self.matrix[len(self.matrix) - 1 - i][i])

    def prepare_output_message(self):
        primary_diagonal = ', '.join(str(x) for x in self.primary_diagonal)
        secondary_diagonal = ', '.join(str(x) for x in reversed(self.secondary_diagonal))
        self.output_message = f'Primary diagonal: {primary_diagonal}. Sum: {sum(self.primary_diagonal)}'
        self.output_message += f'\nSecondary diagonal: {secondary_diagonal}. Sum: {sum(self.secondary_diagonal)}'

    def __repr__(self):
        return self.output_message


if __name__ == '__main__':
    print(Diagonals())
