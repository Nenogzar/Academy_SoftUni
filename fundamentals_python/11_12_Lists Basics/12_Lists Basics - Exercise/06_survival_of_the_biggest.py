# 6. Оцеляване на най-големите
# Напишете програма, която получава списък от цели числа (разделени с един интервал) и число n.
# Числото n представлява броя на числата за премахване от списъка.
# Трябва да премахнете най-малките и след това да отпечатате всички числа,
# които са останали в списъка, разделени със запетая и интервал ", ".

numbers = [int(num) for num in input().split()]
n = int(input())

for _ in range(n):
    numbers.remove(min(numbers))
    result = ', '.join(map(str, numbers))
#print(numbers)
print(result)



######################## FROM CEO ##################################

# number = list(map(int, input().strip().split(" ")))
# [number.remove(min(number)) for _ in range(int(input()))]
# print(", ".join(str(x) for x in number))


######################## FROM CEO ##################################

# numbers = list(map(int,input().strip().split(" ")))
# how_many_numbers_to_remove = int(input())
#
# for n in range(how_many_numbers_to_remove):
#     numbers.remove(min(numbers))
# print(", ".join(str(x) for x in numbers))

######################## FROM CEO ##################################

# numbers = list(map(int,input().strip().split(" ")))
# how_many_numbers_to_remove = int(input())
#
# for n in range(how_many_numbers_to_remove):
#     numbers.remove(min(numbers))
# count = 1
# for o in numbers:
#     if count != (len(numbers)):
#         print(f"{o},", end=" ")
#
#     else:
#         print(f"{o}")
#     count += 1



