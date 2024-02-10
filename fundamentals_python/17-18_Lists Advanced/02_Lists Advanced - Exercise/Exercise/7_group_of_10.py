""" 1 """

sequence = list(map(int, input().split(", ")))

max_sequence = max(sequence)

for group_start in range(1, max_sequence+1, 10):
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

number_list = [int(n) for n in input().split(", ")]

for n in range(1, 11):
    check_list = list()
    if len(number_list) != 0:
        [check_list.append(i) for i in number_list if i <= (n * 10)]
        [number_list.remove(o) for o in check_list]
        print(f"Group of {n * 10}'s: {check_list}")