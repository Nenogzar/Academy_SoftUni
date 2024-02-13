capacity = 255
current_liters = 0
line = int(input())

for _ in range(line):
    liters = int(input())

    if current_liters + liters <= capacity:
        current_liters += liters
    else:
        print("Insufficient capacity!")

print(current_liters)


""" I. Shopov"""

# number_of_lines = int(input())
# tank_capacity = 255
# for line in range(number_of_lines):
#     liters_of_water = int(input())
#     if tank_capacity - liters_of_water < 0:  # No enough volume
#         print("Insufficient capacity!")
#         continue
#     tank_capacity -= liters_of_water
# print(255 - tank_capacity)

""" CEO """

# number_of_pipes = int(input())
#
# capacity = 255
# total_capacity_left = 0
#
# for _ in range(number_of_pipes):
#
#     pipe = int(input())
#
#     if capacity - pipe >= 0:
#         capacity -= pipe
#         total_capacity_left += pipe
#
#     else:
#         print("Insufficient capacity!")
#
# print(total_capacity_left)
