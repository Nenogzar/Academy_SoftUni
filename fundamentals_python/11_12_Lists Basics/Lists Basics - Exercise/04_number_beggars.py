# Ще получите 2 реда за въвеждане.
# На първия ред ще получите единичен низ от цели числа, разделени със запетая и интервал ", ".
# На втория ред ще получите брой beggars.
# Вашата задача е да отпечатате списък със сбора на това, което всеки beggars носи вкъщи,
# като приемем, че всички се редуват редовно, от първия до последния номер в списъка.
# Например:[1, 2, 3, 4, 5] за 2 просяци ще върне резултат от 9 и 6, като първият взема [1, 3, 5],вторият събира [2, 4].
# [1, 2, 3, 4, 5] за  3-ма просители би дал по-добър резултат за втория просяк:
# 5, 7 и 3, тъй като те съответно ще вземат [1, 4], [2, 5] и [3].
# Speps

beggars_list = input().split(",")
beggars_list = [int(num) for num in beggars_list]
range_beggars = int(input())
sum_parts = [0] * range_beggars

for i, num in enumerate(beggars_list):
    index = i % range_beggars
    sum_parts[index] += num

# for i in range(len(beggars_list)):
#     sums[i % range_beggars] += beggars_list[i]


print(sum_parts)

######################## FROM CEO ##################################

# first_line = input()
# second_line = int(input())
#
# first_line = first_line.split(",")
# total_list = list()
# old_list = list()
# length_of_first = len(first_line)
#
# if length_of_first < second_line:
#     for number in first_line:
#         total_list.append(int(number))
#     for number in range(abs(length_of_first - second_line)):
#         total_list.append(0)
#
#
# elif length_of_first == second_line:
#     for number in first_line:
#         total_list.append(int(number))
#
# else:
#     for number in first_line:
#         old_list.append(int(number))
#     for _ in range(0, second_line):
#         total_list.append(sum(old_list[_::second_line]))
#
# print(total_list)
######################## FROM CEO ##################################
