""" 1 """

sequence = list(map(int, input().split(", ")))

max_sequence = max(sequence)

for group_start in range(1, max_sequence + 1, 10):
    group_end = group_start + 9
    group_numbers = [num for num in sequence if group_start <= num <= group_end]
    print(f"Group of {group_end}'s: {group_numbers}")

""" 2 -  Ivan Shopov """

numbers = [int(number) for number in input().split(", ")]
current_group = 10
while numbers:
    filtered_numbers_for_current_group = [number for number in numbers if number <= current_group]
    print(f"Group of {current_group}'s: {filtered_numbers_for_current_group}")
    current_group += 10
    numbers = [number for number in numbers if number not in filtered_numbers_for_current_group]

""" 3 """

numbers = [int(n) for n in input().split(", ")]
check_numbers = list()

for number in range(1, 10 + 1):
    check_numbers.clear()
    if len(numbers) != 0:
        for num in numbers:
            if int(num) <= number * 10:
                check_numbers.append(num)
        for d in check_numbers:
            numbers.remove(d)

        print(f"Group of {number * 10}'s: {check_numbers}")

""" 4 """


def ten_division(num):
    group = (num // 10) + 1
    if num % 10 == 0:  # 10 falls in the group of 10s according to the exercise
        group -= 1
    return group


numbers_list = [int(i) for i in input().split(', ')]
groups_list = []
for elem in numbers_list:
    if ten_division(elem) not in groups_list:
        groups_list.append(ten_division(elem))
groups_list.sort()

index = 0
for g in groups_list:
    if index + 1 < len(groups_list):
        if groups_list[index + 1] - g > 1 and index + 1 <= len(
                groups_list):  # need to add the missing groups (where there are no numbers)
            groups_list.insert(index + 1, g + 1)
    index += 1
    print(f"Group of {g}0's: {[x for x in numbers_list if ten_division(x) == g]}")


""" 5 whir dictionary """
list_numbers = [int(x) for x in input().split(", ")]
sorted_groups = {}
group = 0

while True:
    if not list_numbers:
        break

    if max(list_numbers) > group:
        group += 10

    sorted_groups[group] = [num for num in list_numbers if num <= group]
    list_numbers = [x for x in list_numbers if x > group]

for key, value in sorted_groups.items():
    print(f"Group of {key}'s: {value}")

""" 6 """