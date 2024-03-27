def char_pyramid(r):
    for i in range(r):
        for j in range(r-i):
            print(" ", end="")
        for k in range(i+1):
            print(chr(122 - k), end="")
        for l in range(i):
            print(chr(122 - l), end="")
        print()

char_pyramid(int(input("Enter number of rows: ")))
