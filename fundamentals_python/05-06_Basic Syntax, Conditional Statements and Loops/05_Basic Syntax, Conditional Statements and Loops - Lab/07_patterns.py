# Write a program that receives a number and creates the following pattern.
# The number represents the largest count of stars on one row.
""" 1 """
# n = int(input())
#
# for i in range(1, n*2):
#     if i <= n:
#         width = i
#     else:
#         width = n*2 - i
#     print('*' * width)
""" 2 """
# n = int(input("Enter a number: "))
#
# # Loop from 1 to n
# for i in range(1, n + 1):
#     print("*" * i + " " * (n - i))
# for i in range(n - 1, 0, -1):
#     print("*" * i + " " * (n - i))

""" 3 heart """

scale_x = 0.04
scale_y = 0.1
for y in range(20, -20, -1):
    line = ''
    for x in range(-30, 30):
        if (((x * scale_x) ** 2 + (y * scale_y) ** 2 - 1) ** 3 - (x * scale_x) ** 2 * (y * scale_y) ** 3) <= 0:
            line += '*'
        else:
            line += ' '
    print(line)

