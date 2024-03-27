# def pattern(row):
#     number = 1
#     for num in range(1, row + 1):
#         for col in range(1, num + 1):
#             print(num, end=" ")
#             number += 1
#         print()
#
#
# row = int(input("колко реда "))
# pattern(row)
#
# """
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# """
#
#
# ######################################
#
# def pattern(row):
#     number = 1
#     for num in range(1, row + 1):
#         for col in range(num):
#             print(number, end=" ")
#             number += 1
#         print()
#
#
# row = int(input("Колко реда? "))
# pattern(row)
#
# """ OR """
#
#
# def pattern(row):
#     number = 1
#     for num in range(1, row + 1):
#         print(' '.join(str(number + col) for col in range(num)))
#         number += num
#
#
# row = int(input("Колко реда? "))
# pattern(row)
#
# """
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# """
#
#
# ###################################
#
# def pattern(row):
#     number = 1
#     for num in range(1, row + 1):
#         print(' '.join(str(number + col) for col in range(num)))
#         number += 1
#
#
# row = int(input("Колко реда? "))
# pattern(row)
#
# """
# 1
# 2 3
# 3 4 5
# 4 5 6 7
# """

###################################
def print_pattern(rows):
    for i in range(rows):
        num = 1
        for j in range(1, rows + 2):
            if num == 0:
                continue
            else:
                print(num, end=" ")
                num = num *(i+1-j) // j
        print()


print_pattern(5)