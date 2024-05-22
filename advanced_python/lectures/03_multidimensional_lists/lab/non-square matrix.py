matrix = []
while True:
    row_input = input()
    if not row_input:
        break
    row_values = list(map(int, row_input.split(", ")))
    matrix.append(row_values)

# Изчисляваме максималния брой колони
max_columns = max(len(row) for row in matrix)

# Допълваме всеки ред с нули до максималния брой колони
for row in matrix:
    padding = max_columns - len(row)
    row.extend([0] * padding)

for nest in matrix:
    print(nest)



"""
input:

1, 2, 3
4
5, 6
7, 8, 9, 10
1, 5
12, 2, 3, 5, 5

"""
