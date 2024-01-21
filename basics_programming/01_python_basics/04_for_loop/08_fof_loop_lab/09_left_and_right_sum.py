number = int(input())
left_sum = 0
right_sum = 0
for i in range(0,number):
    num_l = int(input())
    left_sum += num_l

for i in range(number):
    num_r = int(input())
    right_sum += num_r

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {abs(left_sum - right_sum)}")
