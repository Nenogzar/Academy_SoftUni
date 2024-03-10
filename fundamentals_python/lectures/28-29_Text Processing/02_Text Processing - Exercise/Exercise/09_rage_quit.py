text = input()
result, current_combination = '', ''

for character in range(len(text)):
    if character + 1 < len(text) and text[character].isdigit() and text[character + 1].isdigit():
        current_combination = current_combination * int(text[character:character + 2])
        result += current_combination
        current_combination = ''
    elif text[character].isdigit():
        current_combination = current_combination * int(text[character])
        result += current_combination
        current_combination = ''
    else:
        current_combination += text[character]

result = result.upper()
print(f"Unique symbols used: {len(set(result))}")
print(result)

"""Ivan Shopov"""

text = input()
rage_message, repetitions, sub_string = "", "", ""

for index in range(len(text)):
    if not text[index].isdigit():  # non-numeric symbol
        sub_string += text[index].upper()
    else:  # number of repetitions
        for next_symbols in range(index, len(text)):
            if not text[next_symbols].isdigit():
                break
            repetitions += text[next_symbols]
        rage_message += sub_string * int(repetitions)
        repetitions = ""
        sub_string = ""
print(f"Unique symbols used: {len(set(rage_message))}")
print(rage_message)

"""CEO  """

main_string = input()

current_result, result_show, number = "", "", "",

for index, symbols in enumerate(main_string):
    if not symbols.isdigit():
        current_result += symbols
    elif symbols.isdigit():
        number += symbols
        if index + 1 < len(main_string):
            if main_string[index + 1].isdigit():
                continue
        result_show += int(number) * current_result
        current_result, number = "", ""

result_show = result_show.upper()
print(f"Unique symbols used: {len(set(result_show))}")
print(result_show)
