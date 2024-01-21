number = int(input("Въведете число: "))

if number <= 1:
    print(f"{number} не е просто число")
else:
    is_prime = True
    i = 2

    while i <= number // 2:
        if number % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        print(f"{number} е просто число")
    else:
        print(f"{number} не е просто число")

print("Проверката приключи")

# whit for loop
# number = int(input("Въведете число: "))
#
# # Проверка дали числото е по-малко или равно на 1
# if number <= 1:
#     print(f"{number} не е просто число")
# else:
#     is_prime = True  # Предполагаме, че числото е просто
#
#     # Проверка за делители в интервала [2, number // 2]
#     for i in range(2, number // 2 + 1):
#         if number % i == 0:
#             is_prime = False
#             break
#
#     if is_prime:
#         print(f"{number} е просто число")
#     else:
#         print(f"{number} не е просто число")
#
# print("Проверката приключи")
