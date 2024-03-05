n = int(input())
b = int(input())
binary_representation = bin(n)[2:]
# print(binary_representation)

count_b_digit = binary_representation.count(str(b))
binary_digit_str = "zeroes" if b == 0 else "ones"
print(f"{n} -> {binary_representation}")
print(count_b_digit)


""" """
n = int(input())
b = int(input())
binary_list = []

while n > 0:
    remainder = n % 2
    binary_list.insert(0, remainder)
    n = n // 2


binary_str = ''.join(map(str, binary_list))
count_b_digit = binary_str.count(str(b))

print(f"{binary_str}") # Hex
print(count_b_digit)  # count

