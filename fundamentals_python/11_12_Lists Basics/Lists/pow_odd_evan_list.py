# evan_list = []
# odd_list = []
#
# for num in range(1, (int(input("дължината на списъците : ")))+1):
#     evan_list.append(num) if pow(num, 1, 3) == 0 else odd_list.append(num)
#
# print(evan_list)
# print(odd_list)


wanted_list = []
rest_list = []
len_list = int(input("len of list: "))
steps = int(input("what is the power: "))
for number in range(1, len_list+1):
    if pow(number, 10, steps) == 0:
        wanted_list.append(number)
    else:
        rest_list.append(number)
print(f"{wanted_list = }")
print(f"{rest_list = }")