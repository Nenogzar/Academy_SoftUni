n = int(input())
b = int(input())
binary_representation = bin(n)[2:]
# print(binary_representation)

count_b_digit = binary_representation.count(str(b))
binary_digit_str = "zeroes" if b == 0 else "ones"
print(f"{n} -> {binary_representation}")
print(f"We have {count_b_digit} {binary_digit_str}.")