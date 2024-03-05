number = 0
p = 0

number = int(input())
p = int(input())

bitmask = ~(1 << p)
result = number & bitmask

print(result)
