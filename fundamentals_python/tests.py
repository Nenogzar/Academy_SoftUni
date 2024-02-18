A = list(k for k in range(1, 21) if k % 3 != 0)

B = [2 ** (k // 2) if k % 2 == 0 else 3 ** (k // 2) for k in range(15)]

C = [0 if k == 0 or k == 1 else k ** 2 for k in range(13) if not k in [2, 5, 7]]

alpha = A[::-1]
bravo = B[::2]
charly = B[1::2]

print(f"{A = }")
print(f"{B = }")
print(f"{C = }")
print(f"{alpha = }")
print(f"{bravo = }")
print(f"{charly = }")

''''''''''''''''''''''''


def kvadrat(number):
    return map(lambda num: num ** 2, number)


num1 = [1, 2, 3]
num2 = [3, 4, 5]

squared = map(lambda num: num ** 2, num1)
print(list(squared))

print(list(kvadrat(num2)))
''''''''''''''''''''''''


def double_even(num):
    if num % 2 == 0:
        return num * 2
    else:
        return num


numbers1 = [x for x in range(1, 12)]
print(f"{numbers1 = }")

result = list(map(double_even, numbers1))
print(f"{result = }")
''''''''''''''''''''''''


def squar(number):
    return number ** 2


numbers2 = [num for num in range(1, 6)]

squared2 = list(map(squar, numbers2))
print(squared2)
''''''''''''''''''''''''
first_it = [1, 2, 3, 4]
second_it = [5, 6, 7, 8]
pow_list = list(map(pow, first_it, second_it))

print(f"list {first_it} on pow list {second_it} equal to {pow_list}")

''''''''''''''''''''''''
string_it = ["Processing strings", "with a", "MAP"]
cap_str = list(map(str.capitalize, string_it))
low_str = list(map(str.lower, string_it))
swap_str = list(map(str.swapcase, string_it))
title_str = list(map(str.title, string_it))
upper_str = list(map(str.upper, string_it))

print(f"{cap_str = }:\n{low_str = }:\n{swap_str = }:\n{title_str = }:\n{upper_str = }")

''''''''''''''''''''''''

def remove_symbols_and_spaces(text):
    # Заместваме празните полета с '_'
    result = '_'.join(word for word in text.split() if word.isalnum())
    return result

original_text = "This is an example text! 123 #$%^"
cleaned_list = list(map(str, remove_symbols_and_spaces(original_text)))
print(f"{cleaned_list = }" )
print(f"clear text = {remove_symbols_and_spaces(original_text)}")

''''''''''''''''''''''''

original_text = ["processing..", "...strings", "with....", "..map.."]

def remove_symbols_and_spaces_from_list(word):
    return ''.join(filter(str.isalnum, word))

cleaned_text = list(map(remove_symbols_and_spaces_from_list, original_text))

print(cleaned_text)


''''''''''''''''''''''''

def rotate_chr(c):
    rot_by = 3
    c = c.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # Keep punctuation and whitespace
    if c not in alphabet:
        return c
    rotated_pos = ord(c) + rot_by
    # If the rotation is inside the alphabet
    if rotated_pos <= ord(alphabet[-1]):
        return chr(rotated_pos)
    # If the rotation goes beyond the alphabet
    return chr(rotated_pos - len(alphabet))
message = "My secret message goes here."
secret = "".join(map(rotate_chr, message))
print(secret)

def rotate_back(c):
    rot_by = 3
    c = c.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # Keep punctuation and whitespace
    if c not in alphabet:
        return c
    rotated_pos = ord(c) - rot_by
    # If the rotation is inside the alphabet
    if rotated_pos >= ord(alphabet[0]):
        return chr(rotated_pos)
    # If the rotation goes beyond the alphabet
    return chr(rotated_pos + len(alphabet))

encoded_message = secret
decoded = "".join(map(rotate_back, encoded_message))
print(decoded)
