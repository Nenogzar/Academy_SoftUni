div = int(input())
bound = int(input())

for num in range(bound, div - 1, -1):
    if num % div == 0:
        break
print(num)

""" 2 """

number_divisor = int(input())
number_boundary = int(input())

target_number = 0
for number in range(1, number_boundary + 1):
    number_check = number / number_divisor
    if 0 < number <= number_boundary and number_check.is_integer():
        target_number = number

print(target_number)

""" 3 """
divisor = int(input())
boundary = int(input())

result = (boundary // divisor) * divisor
print(result)