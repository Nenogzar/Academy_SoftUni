# sequence = list(map(int, input().split(", ")))
#
#
# for group_start in range(1,101,10):
#     group_end = group_start + 9
#     group_numbers = [num for num in sequence if group_start <= num <= group_end]
#
#     if not any(group_start <= num <= group_end + 9 for num in sequence):
#         continue
#
#     print(f"Group of {group_end}'s: {group_numbers}")

""" 1 """

sequence = list(map(int, input().split(", ")))

max_sequence = max(sequence)

for group_start in range(1, max_sequence+1, 10):
    group_end = group_start + 9
    group_numbers = [num for num in sequence if group_start <= num <= group_end]
    print(f"Group of {group_end}'s: {group_numbers}")
