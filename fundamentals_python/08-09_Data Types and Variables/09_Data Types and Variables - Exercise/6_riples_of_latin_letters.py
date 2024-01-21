""" 1 """
simbol = int(input())

for first_symbol in range(simbol):
    for second_symbol in range(simbol):
        for third_symbol in range(simbol):
            combination = chr(97 + first_symbol) + chr(97 + second_symbol) + chr(97 + third_symbol)
            print(combination)



""" 2 """
# simbol = int(input())
# for first_simbols in range(simbol):
#     for second_simbols in range(simbol):
#         for third_simbols in range(simbol):
#             print(f"{chr(97+first_simbols)}{chr(97+second_simbols)}{chr(97+third_simbols)}")

