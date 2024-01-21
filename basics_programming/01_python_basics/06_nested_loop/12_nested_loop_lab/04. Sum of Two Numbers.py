number_1 = int(input())
number_2 = int(input())
num_magik = int(input())
count_num = 0
found_magik = False  # the flag

for num_1 in range(number_1, number_2 + 1):
    for num_2 in range(number_1, number_2 + 1):
        count_num += 1
        # print("num_1 - ", num_1, "num_2 - ", num_2)
        multiplication = num_1 + num_2
        # print("multiplication - ", multiplication)
        if multiplication == num_magik:
            print(f"Combination N:{count_num} ({num_1} + {num_2} = {num_magik})")
            found_magik = True  # Set the flag to True
            break
    if found_magik:  # Check the flag
        break

if not found_magik:
    print(f"{count_num} combinations - neither equals {num_magik}")