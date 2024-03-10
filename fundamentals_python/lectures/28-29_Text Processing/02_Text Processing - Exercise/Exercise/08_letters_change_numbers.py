from icecream import ic


from string import ascii_lowercase

text = input().split()
total_sum = 0
alphabet = " " + ascii_lowercase

for string in text:
    first_letter = string[0]
    last_letter = string[-1]
    number = int(string[1:-1])

    if string[0].isupper():
        total_sum += number / alphabet.index(first_letter.lower())

    elif string[0].islower():
        total_sum += number * alphabet.index(first_letter)

    if string[-1].isupper():
        total_sum -= alphabet.index(last_letter.lower())

    elif string[-1].islower():
        total_sum += alphabet.index(last_letter)

print(f"{total_sum:.2f}")

""" Ivan Shopov"""


text = input().split()
sum = 0

for word in text:
    char = word[0]
    location = ord(char)

    if location >= 65 and location <= 90:
        location -= 64
    else:
        location -= 96
    string_as_a_digit = float(word[1:-1])

    if char.isupper():
        string_as_a_digit /= location
    else:
        string_as_a_digit *= location
    char = word[-1]
    location = ord(char)

    if location >= 65 and location <= 90:
        location -= 64
    else:
        location -= 96
    if char.isupper():
        string_as_a_digit -= location
    else:
        string_as_a_digit += location
    sum += string_as_a_digit
print(f"{sum:.2f}")


""" Ivan Shopov """

all_strings = input().split()
total_sum = 0
for current_string in all_strings:
    first_letter = current_string[0]
    last_letter = current_string[-1]
    current_number = int(current_string[1: len(current_string) -1])

    if first_letter.isupper():
        first_letter_position = ord(first_letter) - 64
        total_sum += current_number / first_letter_position

    elif first_letter.islower(): #else:
        first_letter_position = ord(first_letter) - 96
        total_sum += current_number * first_letter_position

    if last_letter.isupper():
        last_letter_position = ord(last_letter) - 64
        total_sum -= last_letter_position

    elif last_letter.islower(): #else:
        last_letter_position = ord(last_letter) - 96
        total_sum +=  last_letter_position

print(f"{total_sum:.2f}")


""" CEO """

import re

main_string = re.sub("\\s+", " ", input()).split()
# ic(main_string)
total = 0
for string in main_string:
    numbers = int(string[1:-1])

    if string[0].isupper():
        first_result = numbers / ((ord(string[0].lower())) - 96)
    else:
        first_result = numbers * ((ord(string[0].lower())) - 96)

    if string[-1].isupper():
        second_result = first_result - ((ord(string[-1].lower())) - 96)
    else:
        second_result = first_result + ((ord(string[-1].lower())) - 96)
    total += second_result

print(f"{total:.2f}")

""" """
cleaned_strings = [s.strip() for s in input().split()]
# ic(cleaned_strings)
all = 0

for string in cleaned_strings:
    number = int(string[1:-1])

    if string[0].isupper():
        f_result = number / ((ord(string[0].lower()))-96)
    else:
        f_result = number * ((ord(string[0].lower()))-96)
    if string[-1].isupper():
        s_result = f_result - ((ord(string[-1].lower()))-96)
    else:
        s_result = f_result + ((ord(string[-1].lower()))-96)
    all += s_result
print(f"{all:.2f}")
