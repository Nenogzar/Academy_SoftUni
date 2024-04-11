rows = int(input())
matrix = []

# Get the elements for each column
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)
    # print(matrix)

# Read the commandss

while True:
    command = input()
    if command == "END":
            break



    # Split the command into parts
    parts = command.split()

    # Get the operation type, row, column, and value
    operation = parts[0]
    row = int(parts[1])
    col = int(parts[2])
    value = int(parts[3])

    # Check if the coordinates are valid
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
        print("Invalid coordinates")
        continue

    # Perform the operation
    if operation == "Add":
        matrix[row][col] += value
    elif operation == "Subtract":
        matrix[row][col] -= value


# Print the matrix
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()


"""This program first gets the number of rows and creates an empty matrix. 
Then, it gets the elements for each column and stores them in the matrix. 
Next, it processes the commands until it receives "END". 
Each command is split into parts, and the operation type, row, column, and value are extracted. 
Then, the program checks if the coordinates are valid. 
If they are valid, the program performs the operation (addition or subtraction) on the matrix. 
Finally, the program prints the modified matrix."""