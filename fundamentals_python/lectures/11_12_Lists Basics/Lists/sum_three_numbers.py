# a = int(input("a:"))
# b = int(input("b:"))
# c = int(input("c:"))
#
# x1 = a + b
# x2 = b + c
# x3 = c + a
#
# res1 = c + x1
# res2 = a + x2
# res3 = b + x3
#
# print(res1, res2, res3)

""""List"""

# num = list()
# total = 0
# for number in range(3):
#     inp = input(f'Enter numbers {number}: ')
#     num.append(int(inp))
# print(num)
# total1 = sum(num)
# print(f"{total1 = }")


""""NEXT"""

elements = list(map(int, input('input').split()))
total_list = sum(elements)
print(f"{total_list = }")
list_number = [total_list] * len(elements)
print(f"{list_number = }")
#
# """""next"""
#
# chisla = input("Enter the number of the list whit space-separated: ").split()
# chisla_list_int = [int(i) for i in chisla]
# sum_arguments = sum(chisla_list_int)
# print(f"{sum_arguments = }")
# me_list_chisla = [sum_arguments] * len(chisla_list_int)
#
# print(me_list_chisla)
