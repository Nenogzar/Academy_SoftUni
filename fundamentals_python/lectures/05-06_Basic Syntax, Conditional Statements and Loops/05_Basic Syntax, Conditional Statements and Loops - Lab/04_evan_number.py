""" 1 """
# for i in range(int(input())):
#     num = int(input())
#     if not num % 2 == 0:  # if num % 2 != 0:
#         print(f"{num} is odd!")
#         break
# else:
#     print("All numbers are even.")


""" 2   whit list"""

number = int(input())
numbers = []
for _ in range(number):
    num = int(input())
    numbers.append(num)

if all(n % 2 == 0 for n in numbers):
    print("All numbers are even.")
else:
    for n in numbers:
        if n % 2 != 0:
            print(f"{n} is odd!")
            break
