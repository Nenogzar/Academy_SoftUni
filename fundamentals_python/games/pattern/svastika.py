"""Patern Swastika """
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