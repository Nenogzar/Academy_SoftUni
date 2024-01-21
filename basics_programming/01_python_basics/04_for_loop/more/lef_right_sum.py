# прочита цяло число - n, след което два пъти едно след друго прочита числа
# чийто брой е равен на n. сумира двете поредици и ги сравнява.
import math
n = int(input("Въведете n"))
left_sum = 0
right_sum=0

for i in range(0,n):
    left_num=int(input("ляво: "))
    left_sum+=left_num
for i in range(0,n):
    right_num=int(input("дясно: "))
    right_sum+=right_num
if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {right_sum-left_sum}")