rows = int(input("Numbers of rows: "))
cols = int(input("Numbers of columns: "))

for row in range(rows):
    for col in range(cols):
        if (row+col) %2 == 0:
            print("X", end=" ")
        else:
            print("O", end=" ")
    print()
