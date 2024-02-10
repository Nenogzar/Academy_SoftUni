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