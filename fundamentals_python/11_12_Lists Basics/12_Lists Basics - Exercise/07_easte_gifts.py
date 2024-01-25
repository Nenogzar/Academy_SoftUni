# Създайте програма, която ви помага да планирате подаръците за вашите приятели и семейство. Първо, вие ще получите
# подаръците, които планирате да купите, на един ред, разделени с интервал, в следния формат:
# „{gift1} {gift2} {gift3}...{giftn}“
# След това ще започнете да получавате команди, докато не прочетете съобщението "No Money"
# Има три възможни команди:
#   "OutOfStock {gift}"
#       * Намерете подаръците с това име във вашата колекция, ако има такива, и променете техните стойности на "None".
#   "Required {gift} {index}"
#       * Ако индексът е валиден, заменете подаръка в дадения индекс с дадения подарък.
#   "JustInCase {gift}"
#       * Заменете стойността на последния си подарък с този.
# Накрая отпечатайте подаръците на един ред, с изключение на тези със стойност "None",
# разделени с един интервал в формат:
#   "{gift1} {gift2} {gift3} … {giftn}"
# Input / Constraints
#   • На 1-ви ред ще получите имената на подаръците, разделени с един интервал.
#   • На следващите редове, докато не бъде получена командата "No Money", вие ще получавате команди.
#   • Въведеното винаги ще бъде валидно.

names_of_gifts = input().split(" ")
#print(names_of_gifts)

command = input()
while command != "No Money":
    command_type, *other_info = command.split()

    if "OutOfStock" in command_type:

        for i, name in enumerate(names_of_gifts):

            if other_info[-1] == name:
                names_of_gifts[i] = "None"

    elif "Required" in command_type:
        length = len(names_of_gifts)

        if length > int(other_info[-1]) >= 0:
            names_of_gifts[int(other_info[-1])] = other_info[0]

    elif "JustInCase" in command_type:

        names_of_gifts[-1] = other_info[-1]
    command = input()

print(" ".join(x for x in names_of_gifts if x != "None"))


####################### FROM CEO #######################################

# names_of_gifts = input().split(" ")
#
#
# command = input()
# while command != "No Money":
#     command_type, *other_info = command.split()
#     if "OutOfStock" in command_type:
#         for i, name in enumerate(names_of_gifts):
#             if other_info[-1] == name:
#                 names_of_gifts[i] = "None"
#     elif "Required" in command_type:
#         length = len(names_of_gifts)
#         if length > int(other_info[-1]) >= 0:
#             names_of_gifts[int(other_info[-1])] = other_info[0]
#     elif "JustInCase" in command_type:
#         names_of_gifts[-1] = other_info[-1]
#     command = input()
#
# print(" ".join(x for x in names_of_gifts if x != "None"))
