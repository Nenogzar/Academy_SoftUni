""" From CIO"""
text = input()

check_for_wolf = text.split(", ")
check_for_number = len(check_for_wolf) - 1

for animal in check_for_wolf:

    if animal == "wolf" and check_for_number == 0:
        text_to_print = "Please go away and stop eating my sheep"

    elif animal == "wolf":
        text_to_print = f"Oi! Sheep number {check_for_number}! You are about to be eaten by a wolf!"

    check_for_number -= 1

print(text_to_print)

""" 1 """

# sheeps = list(reversed(input().split(', ')))
# print('Please go away and stop eating my sheep' if sheeps[0] == 'wolf' else f'Oi! Sheep number {sheeps.index("wolf")}! You are about to be eaten by a wolf!')