sequence = list(map(int, input().split(", ")))


for group_start in range(0, 100, 10):
    group_end = group_start + 10
    group_numbers = [num for num in sequence if group_start <= num <= group_end]

    if not any(group_start <= num <= group_end + 10 for num in sequence):
        break

    print(f"Group of {group_end}'s: {group_numbers}")