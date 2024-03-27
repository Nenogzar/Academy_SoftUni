
> pyramid whit numbers
```pycon
def pattern(row):
    number = 1
    for num in range(1, row + 1):
        for col in range(1, num + 1):
            print(num, end=" ")
            number += 1
        print()


row = int(input("how many lines: "))
pattern(row)
```
output:
```pycon
1
2 2
3 3 3
4 4 4 4
```
```pycon
def pattern(row):
    number = 1
    for num in range(1, row + 1):
        # print(' '.join(str(number + col) for col in range(num)))
        # number += num
        # OR
        for col in range(num):
            print(number, end=" ")
            number += 1
        print()


row = int(input("how many lines: "))
pattern(row)
```
output:
```pycon
1 
2 3 
4 5 6 
7 8 9 10
```



> swastik

```pycon
def print_swastika(rows, cols):
    for i in range(rows):
        for j in range(cols):
            if i < rows // 2:
                if j < cols // 2:
                    if j == 0:
                        print("#", end=" ")
                    else:
                        print(" ", end=" ")
                elif j == cols // 2:
                    print("#", end=" ")
                else:
                    if i == 0:
                        print("#", end=" ")
                    else:
                        print(" ", end=" ")
            elif i == rows // 2:
                print("#", end=" ")
            else:
                if j > cols // 2:
                    if j == cols - 1:
                        print("#", end=" ")
                    else:
                        print(" ", end=" ")
                elif j == cols // 2:
                    print("#", end=" ")
                else:
                    if i == rows - 1:
                        print("#", end=" ")
                    else:
                        print(" ", end=" ")
        print()

# For correct figure, enter only odd values for column and row
print_swastika(5, 5)
```
output:
```pycon
#   # # # 
#   #     
# # # # # 
    #   # 
# # #   # 
```