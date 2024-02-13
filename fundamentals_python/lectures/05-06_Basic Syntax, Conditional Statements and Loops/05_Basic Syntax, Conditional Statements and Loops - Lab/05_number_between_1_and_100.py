num = float(input())
""" 1 """
# while num < 1 or num >100:
#     num = float(input())
# print(f"The number {num} is between 1 and 100")

""" 2 """

while True:
    if 1 < num and num <100:
        print(f"The number {num} is between 1 and 100")
        break
    else:
        num = float(input())

