#################################### TASK CONDITION ############################
"""
                    5.	Primary Diagonal
Write a program that finds the sum of all numbers in a matrix's primary 
diagonal (runs from top left to bottom right). On the first line, 
you will receive an integer N – the size of a square matrix. The next N 
lines holds the values for each column - N numbers, separated by a single space. 

____________________________________________________________________________________________
Example_01

Input
3
11 2 4
4 5 6
10 8 -12	

Output
4	

____________________________________________________________________________________________
Example_02

Input
3
1 2 3
4 5 6
7 8 9	

Output
15

"""

    ##########: variant 1 :##########

rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
sum_of_diagonal = 0
for row in range(rows):
    sum_of_diagonal += matrix[row][row]
print(sum_of_diagonal)

    ##########: variant 2 :##########

matrix = []
matrix_size = int(input())
for row in range(matrix_size):
    numbers = list(map(int, input().split()))
    matrix.append(numbers)
result = 0
for index, col in enumerate(zip(*matrix)):
    result += col[index]
print(result)

    ##########: variant 3 :###########

n = int(input())

matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

primary_sum = 0
for i in range(n):
    primary_sum += matrix[i][i]

print(primary_sum)


##########: variant 4 - Class:##########
class PrimaryDiagonal:

    def __init__(self):
        self.rows = int(input())
        self.matrix = []
        self.sum_of_diagonal = 0
        self.main_meth()

    def main_meth(self):
        self.create_matrix()
        self.find_sum_of_diagonal()

    def create_matrix(self):
        for row in range(self.rows):
            line = [int(x) for x in input().split()]
            self.matrix.append(line)

    def find_sum_of_diagonal(self):
        for index in range(len(self.matrix)):
            self.sum_of_diagonal += self.matrix[index][index]

    def __repr__(self):
        return str(self.sum_of_diagonal)


if __name__ == '__main__':
    print(PrimaryDiagonal())



