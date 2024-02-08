list_num = [float(n) for n in input().split()]

num_dict = {}

for num in list_num:
    if num not in num_dict:
        num_dict[num] = 1
    else:
        num_dict[num] += 1

result_list = []

for num in list_num:
    if num_dict[num] > 1:
        # Проверка дали вече не е добавен в текущия вложен списък
        if not any(abs(num) == abs(item[0]) for item in result_list):
            result_list.append([num])
        else:
            for item in result_list:
                if abs(num) == abs(item[0]):
                    item.append(num)
                    break
    else:
        result_list.append([num])

print(result_list)
