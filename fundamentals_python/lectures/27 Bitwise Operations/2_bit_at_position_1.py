n = int(input())

bit = bin(n)[2:]
bit_position = bit[-2]


print(f"{bit} -> {bit_position}")

print(bit_position)
