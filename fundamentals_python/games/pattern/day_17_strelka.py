number_of_rows = int(input("Enter the number of rows: "))
for i in range(0, number_of_rows):
    for j in range(0, number_of_rows):
        if i+j == number_of_rows-1 or i<=j:
            print("* ", end=" ")
        else:
            print("  ", end=" ")
    print()

