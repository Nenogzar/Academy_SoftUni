num = int(input("Въведете брой редове: "))

i, j = 0, 0
for i in range(0, num):
    print()
    for j in range(0, i + 1):
        print("*", end="")
