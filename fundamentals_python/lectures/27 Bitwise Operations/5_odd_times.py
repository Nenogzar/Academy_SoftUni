numbers = list(map(int, input().split()))
result = 0

for num in numbers:
    result ^= num

print(f"The number occurring an odd number of times is: {result}")
