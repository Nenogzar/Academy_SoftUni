# import re
#
# inp_str = input().split(", ")
#
# while True:
#     race = input()
#     if race == "end of race":
#         break
#
#
#     # Извличане на буквите
#     letters = re.findall(r'[A-Za-z]', race)
#     name = ''.join(letters)
#
#     # Извличане на цифрите
#     digits = re.findall(r'\d', race)
#     achievement = sum(map(int, digits))
#
#     print(f"Име: {name} Постижение: {achievement}")
#
# from icecream import ic
import re

participants = input().split(", ")

results = {}

while True:
    race = input()
    if race == "end of race":
        break

    # Name and distance r string
    name = ''.join(re.findall(r'[A-Za-z]', race))
    distance = sum(map(int, re.findall(r'\d', race)))

    #ic(name)
    #ic(distance)

    # use a dictionary
    if name in participants:
        if name not in results:
            results[name] = 0
        results[name] += distance
        #ic(results)

# sort descending

sorted_results = dict(sorted(results.items(), key=lambda item: item[1], reverse=True))
#ic(dict(sorted(results.items(), key=lambda item: item[1], reverse=True)))

# take a first 3 position
top_three = list(sorted_results.keys())[:3]
#ic(list(sorted_results.keys())[:3])

print(f"1st place: {top_three[0]}")
print(f"2nd place: {top_three[1]}")
print(f"3rd place: {top_three[2]}")
