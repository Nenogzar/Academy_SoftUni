rows = int(input())
matrix = []

for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)
    # print(matrix)

command = input()
while command != "END":

    parts = command.split()
    operation = parts[0]
    row = int(parts[1])
    col = int(parts[2])
    value = int(parts[3])

    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
        print("Invalid coordinates")
        continue

    if operation == "Add":
        matrix[row][col] += value
    elif operation == "Subtract":
        matrix[row][col] -= value

    command = input()


for row in matrix:
    for element in row:
        print(element, end=" ")
    print()