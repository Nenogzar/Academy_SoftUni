n = int(input())
num_max = None
num_min = None

for i in range(n):
    num = int(input())
    if num_max is None or num >= num_max:
        num_max = num
    if num_min is None or num <= num_min:
        num_min = num

print(f"Max number: {num_max}")
print(f"Min number: {num_min}")
