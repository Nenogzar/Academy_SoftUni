rows = 5
for row in range(1, rows + 1):
    print(" " * (rows - row) + "* " * row)
for row in range(rows - 1, 0, -1):
    print(" " * (rows - row) + "* " * row)