# number = int(input())
# print("Devision by 1")
# k = 1
# while k < number // 2:
#     k += 1
#     if number % k != 0:
#         continue
#     print("Devision by:", k)
# print("Devision by ", number)


# whit for loop
number = int(input("input number: "))
#print("Деление на 1")
for k in range(1, number // 2 + 1):
    if number % k != 0:
        continue
    print("Devision by:", k)
print("Devision by:", number)
