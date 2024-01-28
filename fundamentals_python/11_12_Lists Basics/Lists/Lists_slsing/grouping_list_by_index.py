# input_list = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
# output_list = []
#
# for i in range(len(input_list[0])):
#     output_list.append([])
#
#     for j in range(len(input_list)):
#         output_list[i].append(input_list[j][i])
#
# # a, b, c = output_list[0], output_list[1], output_list[2]
# # print(a, b, c)
#
# for row in output_list:
#     print(row)

"""" """

input_list = eval(input("Въведете матрицата: "))

num_rows = len(input_list)
num_cols = len(input_list[0])

# Транспониране на матрицата
output_list = []
for i in range(num_cols):
    output_list.append([input_list[j][i] for j in range(num_rows)])

# Присвояване на променливи
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(min(num_cols, len(alphabet))):
    locals()[alphabet[i]] = output_list[i]

# Отпечатване на променливите
for i in range(min(num_cols, len(alphabet))):
    print(f"{alphabet[i]} = {locals()[alphabet[i]]}")