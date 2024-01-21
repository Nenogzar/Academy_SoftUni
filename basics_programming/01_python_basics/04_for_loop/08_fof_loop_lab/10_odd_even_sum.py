numbers_of_num = int(input())
odd_sum = 0
even_sum = 0
for num in range(numbers_of_num):
    number = int(input())
    if num % 2 == 0:
        even_sum += number
    else:
        odd_sum += number

different = even_sum - odd_sum
if even_sum == odd_sum:
    print("Yes" )
    print(f"Sum = {even_sum}")
else:
    print("No" )
    print(f"Diff = {abs(different)}")
