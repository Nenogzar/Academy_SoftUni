main_string = input().split(">")

show_result = ""
what_left = 0
for letter in main_string:
    if len(letter) > 1 and any(map(str.isdigit, letter)):
        what_left += (int(letter[0]) - 1)
        if what_left >= len(letter):
            show_result += ">"
        else:
            show_result += ">" + letter[1 + what_left:]
            what_left = 0
    elif len(letter) == 1 and letter.isdigit():
        if int(letter) > 1:
            what_left += (int(letter) - 1)
        show_result += ">"
    else:
        show_result += letter

print(show_result)


"""Ivan Shopov """

some_string = input()
final_string = ""
strength = 0
for index in range(len(some_string)):
    # Explosion
    if strength > 0 and some_string[index] != ">":
        strength -= 1
    # > mark
    elif some_string[index] == ">":
        final_string += some_string[index]
        strength += int(some_string[index + 1])
    # No explosion, no > mark
    else:
        final_string += some_string[index]
print(final_string)

