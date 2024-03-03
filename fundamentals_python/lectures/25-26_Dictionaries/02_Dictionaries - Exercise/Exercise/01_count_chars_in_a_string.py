text = input()
letters = {}
for char in text:
    if char != " ":
        if char not in letters.keys():
            letters[char] = 1
        else:
            letters[char] += 1
for key, value in letters.items():
    print(f"{key} -> {value}")


""" """

# def count_letter(current_text):
#     char_dict = {}
#
#     for word in current_text:
#         for letter in word:
#             if letter not in char_dict:
#                 char_dict[letter] = 1
#             else:
#                 char_dict[letter] += 1
#     return char_dict
#
#
#
# input_str = input().split(" ")
# char_dict = count_letter(input_str)
#
# for k, v, in char_dict.items():
#     print(f"{sorted({k})} -> {v}")

""" """
characters = input().replace(" ", "")

character_count = {}

for character in characters:
    character_count[character] = character_count.get(character, 0) + 1

# for key, value in character_count.items():
#     print(f"{key} -> {value}")
#  OR
[print(f"{keys} -> {value}") for keys, value in character_count.items()]