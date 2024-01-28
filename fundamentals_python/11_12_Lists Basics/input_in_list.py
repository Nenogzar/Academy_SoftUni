""" stre to int"""
str_list = []
list_one = input().split(", ")
for num in list_one:
    number = int(num)
    str_list.append(number)
print(f"{list_one = }")
print(f"{str_list = }")
""" 1 """
list_two = list(map(int, input().strip().split(", ")))
print(f"{list_two = }")

""" 2 """
list_three = [int(number) for number in input().split(", ")]
print(f"{list_three = }")

""" Invert list """
invert_list = [-int(number) for number in input().split(", ")]
print(f"{invert_list = }")

""" 3 """
list_int = list(map(int, input().split(", ")))
print(f"{list_int = }")



""" combo list"""

letters = "AB"
number_list = list(range(1, 11))
combo_list = [f"{leter}-{number}" for leter in letters for number in number_list]
print(f"{combo_list = }")