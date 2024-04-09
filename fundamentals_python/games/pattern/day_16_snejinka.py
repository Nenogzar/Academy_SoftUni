n = int(input("Enter row number: "))
index = n + 1
for i in range(1, index):
    for j in range(1, index):
        if i == index / 2 or j == index / 2 or i == j or i + j == index:
            print("* ", end="")
        print("  ", end="")
    print('')

m = n // 2
for i in range(n):
    for j in range(n):
        c = i == j
        c |= j == n - i - 1
        c |= i == m or j == m
        print("* " if c else '', end="")
    print()
