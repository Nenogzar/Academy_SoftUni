def printpattern(n):
    matrix = [[0] * n for _ in range(n)]
    num = n * n
    top, botton, left, right = 0, n - 1, 0, n - 1

    while top <= botton and left <= right:
        for i in range(left, right + 1):
            matrix[top][i] = num
            num -= 1
        top += 1

        for i in range(top, botton + 1):
            matrix[i][right] = num
            num -= 1
        right -= 1

        for i in range(right, left - 1, -1):
            matrix[botton][i] = num
            num -= 1
        botton -= 1

        for i in range(botton, top - 1, -1):
            matrix[i][left] = num
            num -= 1
        left += 1
    return matrix


def printMatrix(martix):
    for row in matrix:
        for cell in row:
            print(f'{cell:2d}', end=' ')
        print()


n = int(input())
matrix = printpattern(n)
printMatrix(matrix)

# 25 24 23 22 21
# 10  9  8  7 20
# 11  2  1  6 19
# 12  3  4  5 18
# 13 14 15 16 17
