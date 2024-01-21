# Напишете програма, която обявява победителя в автомобилно състезание.
# Ще получите поредица от числа.
# Всяко число представлява времето, което колата трябва да премине през тази стъпка (индекса).
# Ще има две коли.
#       Първият започва от лявата страна, а другият започва от дясната страна.
#       Средният индекс на последователността е финалната линия.
# Изчислете общото време, необходимо на всеки състезател, за да стигне до финалната линия,
# и отпечатайте победителя с общото му време (състезателя с по-малко време).
# Ако имате нула в списъка, трябва да намалите времето на състезателя, който я е достигнал, с 20% (от текущото му време).
# Броят на елементите в последователността винаги ще бъде нечетен. !
# Отпечатайте резултата в следния формат "The winner is {left/right} with total time: {total_time}"
numbers_input = input()
numbers_list = list(map(int, numbers_input.split()))
    # Изчисляване на сумата на индексите
sum_of_indexes = sum(range(len(numbers_list)))
    # Изчисляване на броя на елементите в списъка
num_elements = len(numbers_list)
    # Изчисляване на средния индекс - FINAL
finish_index = int(sum_of_indexes / num_elements)
left_list = numbers_list[:finish_index]
right_list = numbers_list[finish_index+1:][::-1]
# print("left_list", left_list)
# print("right_list", right_list)
left_sum, right_sum = 0, 0
for l in left_list:
    if l == 0:
        left_sum *= 0.8
    else:
        left_sum += l
for r in right_list:
    if r == 0:
        right_sum *= 0.8
    else:
        right_sum += r

if left_sum < right_sum:
    winer = "left"
    winer_time = left_sum
else:
    winer = "right"
    winer_time = right_sum

print(f"The winner is {winer} with total time: {winer_time:.1f}")
##########################################################################
# numbers_input = input()
# numbers_list = list(map(int, numbers_input.split()))
# finish = len(numbers_list) // 2
# left_list = numbers_list[:finish]
# right_list = numbers_list[finish+1:][::-1]
#
# left_sum, right_sum = 0, 0
# for l in left_list:
#     left_sum += l
#     if l == 0:
#         left_sum *= 0.8
#
# for r in right_list:
#     right_sum += r
#     if r == 0:
#         right_sum *= 0.8
#
# print(f"The winner is left with total time: {left_sum:.1f}" if left_sum < right_sum
#       else f"The winner is right with total time: {right_sum:.1f}")
########################################################################
# numbers_list = list(map(int, input().split()))
# finish = len(numbers_list) // 2
# left_list = numbers_list[:finish]
# right_list = numbers_list[finish+1:][::-1]
# left_sum, right_sum = 0, 0
# for l, r in zip(left_list, right_list):
#     left_sum += l
#     if l == 0:
#         left_sum *= 0.8
#     right_sum += r
#     if r == 0:
#         right_sum *= 0.8
#
# print(f"The winner is left with total time: {left_sum:.1f}" if left_sum < right_sum
#       else f"The winner is right with total time: {right_sum:.1f}")

############################### FROM CEO####################################
# sequence_of_numbers = [int(num) for num in input().split()]
#
# first_car = len(sequence_of_numbers) // 2
#
# first_car_score = sum([num if num != 0 else -sum(sequence_of_numbers[:first_car][:pos]) * 0.2 for pos, num in
#                        enumerate(sequence_of_numbers[:first_car])])
# second_car_score = sum([num if num != 0 else -sum(sequence_of_numbers[::-1][:first_car][:pos]) * 0.2 for pos, num in
#                     enumerate(sequence_of_numbers[::-1][:first_car])])
#
# if first_car_score < second_car_score:
#     print(f"The winner is left with total time: {first_car_score:.1f}")
# else:
#     print(f"The winner is right with total time: {second_car_score:.1f}")
###########################################################################

# sequence_of_timers = input().split()
# timers_as_integers = []
# for timer in sequence_of_timers:
#     timers_as_integers.append(int(timer))
# middle_timer = len(timers_as_integers)//2
# left_side = timers_as_integers[0:middle_timer]
# right_side = timers_as_integers[middle_timer+1:][::-1]
#
# left_time = 0
# right_time = 0
# for seconds in left_side:
#     left_time += seconds
#     if seconds == 0:
#         left_time -= 0.2*left_time
# for seconds2 in right_side:
#     right_time += seconds2
#     if seconds2 == 0:
#         right_time -= 0.2 * right_time
#
# if left_time > right_time:
#     print(f'The winner is right with total time: {right_time:.1f}')
# elif left_time<right_time:
#     print(f'The winner is left with total time: {left_time:.1f}')

###########################################################################
#
# sequence_of_numbers = input().split(" ")
#
# car_one_total = 0
# car_two_total = 0
# s_car = sequence_of_numbers
# where_is_split = len(sequence_of_numbers) // 2
#
# for car_one, car_two in zip(sequence_of_numbers[:where_is_split], s_car[::-1]):
#     car_one = int(car_one)
#     car_two = int(car_two)
#     if car_one == 0:
#         car_one_total = car_one_total * 0.8
#     else:
#         car_one_total += car_one
#
#     if car_two == 0:
#         car_two_total = car_two_total * 0.8
#     else:
#         car_two_total += car_two
#
# if car_one_total < car_two_total:
#     print(f"The winner is left with total time: {car_one_total:.1f}")
#
# else:
#     print(f"The winner is right with total time: {car_two_total:.1f}")
#
#
###########################################################################

# sequence_of_numbers = input().split(" ")
#
# first_car = list()
# second_car = list()
# car_one_total = 0
# car_two_total = 0
#
# where_is_split = len(sequence_of_numbers) // 2
# for car_one in sequence_of_numbers[:where_is_split]:
#     first_car.append(float(car_one))
#
# sequence_of_numbers.reverse()
# for car_two in sequence_of_numbers[:where_is_split]:
#     second_car.append(float(car_two))
#
# for one, two in zip(first_car, second_car):
#     if one == 0:
#         car_one_total = car_one_total * 0.8
#     else:
#         car_one_total += one
#
#     if two == 0:
#         car_two_total = car_two_total * 0.8
#     else:
#         car_two_total += two
#
# if car_one_total < car_two_total:
#     print(f"The winner is left with total time: {car_one_total:.1f}")
#
# else:
#     print(f"The winner is right with total time: {car_two_total:.1f}")