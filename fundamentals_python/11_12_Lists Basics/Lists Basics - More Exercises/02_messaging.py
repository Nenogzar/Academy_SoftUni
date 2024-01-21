# На първия ред ще получите поредица от числа, разделени с един интервал.
# На втория ред ще получите низ.
# Вашата задача е да напишете програма, която изпраща съобщение само с помощта на знаци от дадения низ.

# Всеки символ, който програмата добавя към съобщението, трябва да бъде намерен по неговия индекс.

# Индексът, който търсите, е сборът от цифрите на числото от първата последователност.

# Ако индексът е по-голям от дължината на текста, продължете да броите отначало
# (за да имате винаги валиден индекс).

# Когато намерите знак, трябва да го добавите към съобщението и да го премахнете от низа.

# Това означава, че за следващия индекс текстът ще съдържа един знак по-малко.

# Отпечатайте последното съобщение.

# Input:
# 9992 562 8933
# This is some message for you
# Output:
# hey

numbers_input = input()
text_input = input()

message = ""
text_list = list(text_input)

for num in map(int, numbers_input.split()):
    digit_sum = sum(int(digit) for digit in str(num))

    list_index = digit_sum % len(text_list)

    message += text_list[list_index]
    text_list.pop(list_index)

    if len(text_list) == 0:
        break

print(message)
#####################################################################
# numbers_input = input()
# text_input = input()
#
# message = ""
# text_list = list(text_input)
#
# for num in map(int, numbers_input.split()):
#
#     index = sum(int(digit) for digit in str(num)) % len(text_list)
#
#
#     message += text_list[index]
#     text_list.pop(index)
#
#
#     if len(text_list) == 0:
#         break
#
# print(message)
#########################  DEF ########################################
# def generate_message(numbers_input, text_input):
#     message = ""
#     text_list = list(text_input)
#
#     for num in map(int, numbers_input.split()):
#         index = sum(int(digit) for digit in str(num)) % len(text_list)
#         message += text_list[index]
#         text_list.pop(index)
#
#         if len(text_list) == 0:
#             break
#
#     return message
#
# numbers_input = input()
# text_input = input()
# final_message = generate_message(numbers_input, text_input)
# print(final_message)


# 9992 562 8933
# This is some message for you
########################### FROM CEO ##################################
# numbers = input().split()
# string_text = input()
# msg_show = ""
#
# for num in numbers:
#     find_index = sum([int(s_num) for s_num in num])
#     if find_index >= len(string_text):
#         find_index = find_index - len(string_text)
#     msg_show += string_text[find_index]
#     string_text = string_text[:find_index] + string_text[find_index + 1:]
#
# print(msg_show)

########################### FROM CEO ##################################
# numbers = input().split()
# string_text = input()
#
# msg_show = ""
#
# for num in numbers:
#     find_index = 0
#     for s_num in num:
#         find_index += int(s_num)
#     if find_index > len(string_text):
#         find_index = find_index - len(string_text)
#     msg_show += string_text[find_index]
#     string_text = string_text[:find_index] + string_text[find_index + 1:]
#
# print(msg_show)



