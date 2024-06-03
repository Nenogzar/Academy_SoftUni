# message = input().split()
#
# words = []
# for word in message:
#     num, let = "", ""
#     for symbol in word:
#         if symbol.isdigit():
#             num += symbol
#         else:
#             let += symbol
#     if len(let) != 1:
#         let = f"{let[-1]}{let[1:-1]}{let[0]}"
#     words.append(f"{chr(int(num))}{let}")
#
# print(*words, end=' ')


message = input().split()
words, numbers = [], []

# Обхождаме всяка дума във входните данни
for word in message:
    # Инициализираме празни низове за числата и буквите
    num, let = "", ""

    for symbol in word:
        # Проверяваме дали символът е цифра или буква
        if symbol.isdigit():
            # Ако е цифра, добавяме я към низа за числата
            num += symbol
        else:
            # Ако е буква, добавяме я към низа за буквите
            let += symbol

    # Конвертираме числата в цяло число и ги добавяме към списъка с числата
    numbers.append(int(num))

    # Проверяваме дължината на низа за буквите и го променяме, ако не е с дължина 1
    if len(let) != 1:
        let = f"{let[-1]}{let[1:-1]}{let[0]}"

    # Добавяме променения низ за буквите към списъка с думите
    words.append(let)

# Обхождаме списъците с числа и думи паралелно и генерираме изхода
for numer, word in zip(numbers, words):
    print(f"{chr(numer)}{word}", end=" ")

""" """
words = input().split()
result = []

for word in words:
    cur_word = list(word)

    char_code = []
    while cur_word[0].isdigit():
        char_code.append(cur_word.pop(0))

    cur_word.insert(0, chr(int("".join(char_code))))
    cur_word[1], cur_word[-1] = cur_word[-1], cur_word[1]

    result.append("".join(cur_word))

print(" ".join(result))


"""" whit regex """

import re


def decode_word(encoded_word):
    pattern = r'(\d+)([a-zA-Z]+)'
    match = re.match(pattern, encoded_word)

    if match:
        ascii_code = int(match.group(1))
        remaining_chars = list(match.group(2))  # Преобразуваме низа в списък

        first_char = chr(ascii_code)
        remaining_chars[0], remaining_chars[-1] = remaining_chars[-1], remaining_chars[0]
        decoded_word = first_char + "".join(remaining_chars)

        return decoded_word
    return ""


def decode_message(encoded_message):
    words = encoded_message.split()
    decoded_words = [decode_word(word) for word in words]
    return " ".join(decoded_words)


decoded_message = decode_message(input())
print(decoded_message)


""" other one """

message = input()

deciphered_message = []
for word in message.split():
    first_letter = ""
    deciphered_word = []
    for letter in word:
        if letter.isnumeric():
            first_letter += letter
            continue
        deciphered_word.append(letter)

    deciphered_word[0], deciphered_word[-1] = deciphered_word[-1], deciphered_word[0]
    deciphered_word = chr(int(first_letter)) + "".join(deciphered_word)

    deciphered_message.append(deciphered_word)

print(*deciphered_message, sep=" ")
