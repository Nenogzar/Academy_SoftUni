# def remove_vowels(text):
#
#     vowels = ['a', 'o', 'u', 'e', 'i']
#
#     new_text = [char for char in text if char.lower() not in vowels]
#
#     return ''.join(new_text)
#
#
# input_string = input()
#
# print(remove_vowels(input_string))

""" Zahariev """

input_string = input()
vowels = ['a', 'o', 'u', 'e', 'i']
new_test = list()

for char in input_string:
    if char.lower() not in vowels:
        new_test.append(char)

print(new_test)



