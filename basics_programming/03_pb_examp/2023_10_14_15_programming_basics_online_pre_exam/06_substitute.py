# num_k = int(input())
# num_l = int(input())
# num_m = int(input())
# num_n = int(input())
#
# counter_position = 0
# for k in range(num_k, 9):
#     if k % 2 == 0:
#         for l in range(9, num_l - 1, -1):
#             if l % 2 != 0:
#                 for m in range(num_m, 9):
#                     if m % 2 == 0:
#                         for n in range(9, num_n - 1, -1):
#                             if n % 2 != 0:
#                                 first_position = k * 10 + l
#                                 second_position = m * 10 + n
#                                 if first_position != second_position:
#                                     print(f"{k}{l} - {m}{n}")
#                                     counter_position += 1
#                                     if counter_position == 6:
#                                         exit()
#                                 if first_position == second_position:
#                                     print("Cannot change the same player.")


num_k = int(input())
num_l = int(input())
num_m = int(input())
num_n = int(input())

counter_position = 0

for k in range(num_k, 9):
    if k % 2 == 0:
        for l in range(9, num_l - 1, -1):
            if l % 2 != 0:
                for m in range(num_m, 9):
                    if m % 2 == 0:
                        for n in range(9, num_n - 1, -1):
                            if n % 2 != 0:
                                first_position = k * 10 + l
                                second_position = m * 10 + n
                                if first_position != second_position:
                                    print(f"{k}{l} - {m}{n}")
                                    counter_position += 1
                                    if counter_position == 6:
                                        break  # Exit the innermost loop
                                if first_position == second_position:
                                    print("Cannot change the same player.")
                    if counter_position == 6:
                        break  # Exit the third loop
            if counter_position == 6:
                break  # Exit the second loop
    if counter_position == 6:
        break  # Exit the first loop
