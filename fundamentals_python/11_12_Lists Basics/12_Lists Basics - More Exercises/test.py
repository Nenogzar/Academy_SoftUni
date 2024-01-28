code_number = [int(num) for num in input().split(" ")]
code_string = input()
cod_list = []

for code in code_number:
    sum_digits = 0
    for digit in str(code):
        sum_digits += int(digit)
    cod_list.append(sum_digits)

decoded_message = ""
for index in cod_list:
    if len(code_string) == 0:
        break
    current_char = code_string[index % len(code_string)]
    decoded_message += current_char
    code_string = code_string.replace(current_char, "", 1)

print(decoded_message)




