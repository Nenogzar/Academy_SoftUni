def calculate_columns(matrix):
    columns = max(len(row) for row in matrix)
    return columns

def check_valid_index(row, col, rows, columns):
    return row + 1 < rows and col + 1 < columns

def sum_square(matrix, row, col):
    sum_total = 0
    for r in range(row, row + 2):
        for c in range(col, col + 2):
            sum_total += matrix[r][c]
    return sum_total

def find_max_sum(matrix):
    max_sum = {"max number": float('-inf'), "row": 0, "col": 0}
    rows = len(matrix)
    columns = calculate_columns(matrix)

    for row in range(rows - 1):
        for col in range(columns - 1):
            current_sum = sum_square(matrix, row, col)
            if current_sum > max_sum["max number"]:
                max_sum["max number"] = current_sum
                max_sum["row"] = row
                max_sum["col"] = col

    return max_sum

def print_submatrix(matrix, max_sum):
    row, col = max_sum["row"], max_sum["col"]
    for r in range(row, row + 2):
        print(" ".join(map(str, matrix[r][col:col + 2])))

def main():
    matrix = []
    while True:
        row_input = input("Enter row (comma separated values), or press enter to finish: ")
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

    max_sum = find_max_sum(matrix)
    print_submatrix(matrix, max_sum)
    print("Max sum:", max_sum['max number'])

if __name__ == "__main__":
    main()
