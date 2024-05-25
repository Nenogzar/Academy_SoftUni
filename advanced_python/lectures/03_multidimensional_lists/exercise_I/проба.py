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
