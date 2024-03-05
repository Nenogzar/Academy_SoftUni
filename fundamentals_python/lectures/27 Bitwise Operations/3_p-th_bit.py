# dic_number = {}
# for a, b in zip(range(11), range(-1, -11, -1)):
#     dic_number[a] = [b]
#
# number = int(input())
# p = int(input())
#
# binary_number = bin(number)[2:]
# # print(binary_number)
#
# if p in dic_number:
#     searching_bit = int(binary_number[dic_number[p][0]])
#
#     print(searching_bit)
# print(f"{binary_number} -> {searching_bit}")

n = int(input())
p = int(input())
bit_at_position_p = 0


# a. Shift the number p times to the right
shifted_number = n >> p

# b. Find the bit at position 0 using & 1 operator
bit_at_position_p = shifted_number & 1

# c. Save the result in bit_at_position_p
result = bit_at_position_p

# Step 4: Print the result
print(f"The bit at position {p} of {n} is {result}")