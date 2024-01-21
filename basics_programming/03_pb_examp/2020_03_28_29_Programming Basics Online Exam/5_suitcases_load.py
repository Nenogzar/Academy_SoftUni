trunk_capacity = float(input())
count_suitcase = 0
total_volume = 0
while True:
    suitcase_volume = input()
    count_suitcase += 1
    if suitcase_volume == "End":
        print("Congratulations! All suitcases are loaded!")
        break

    if count_suitcase % 3 == 1:
        suitcase_volume = float(suitcase_volume) * 1.1

    total_volume += float(suitcase_volume)

    if total_volume > trunk_capacity:
        print("No more space!")
        break
print(f"Statistic: {count_suitcase - 1} suitcases loaded.")

# lugged_capacity = float(input())
#
# lugged = input()
# suitcases = 0
#
# while lugged != "End":
#     lugged = float(lugged)
#     suitcases += 1
#     added_lugged_space = 0
#     if suitcases % 3 == 0:
#         added_lugged_space = lugged * 0.10
#
#     lugged_capacity -= lugged + added_lugged_space
#
#     if lugged_capacity <= 0:
#         if lugged_capacity != 0:
#             suitcases -= 1
#         print("No more space!")
#
#         break
#     lugged = input()
#
# else:
#     print(f"Congratulations! All suitcases are loaded!")
# print(f"Statistic: {suitcases} suitcases loaded.")







# capacity_lagges = float(input())
# number_lagges = 0
# check_space = 0
#
#
# while True:
#     lagge = input()
#
#     if "End" in lagge:
#         print(f"Congratulations! All suitcases are loaded!\nStatistic: {number_lagges} suitcases loaded.")
#         break
#
#     number_lagges += 1
#     lagges = float(lagge)
#     check_space += + lagges
#
#     if number_lagges % 3 == 0:
#         check_space += lagges * 0.10
#
#     if capacity_lagges < check_space:
#         number_lagges += - 1
#         print(f"No more space!\nStatistic: {number_lagges} suitcases loaded.")
#         break
