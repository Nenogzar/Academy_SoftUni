def encrypt_char(c):
    return chr((ord(c) + 3))

input_string = input()
encrypted_result = ''.join(encrypt_char(char) for char in input_string)
print(encrypted_result)

""" """
def encrypt_char(c):
    return chr((ord(c) + 3))

def encrypt_text(text):
    encrypted_result = ''.join(encrypt_char(char) for char in text)
    return encrypted_result

input_string = input()
print(encrypt_text(input_string))





""" Iwan Shopov"""

# text = input()
# encrypted_text = ""
# for character in text:
#     encrypted_character = chr(ord(character) + 3)
#     encrypted_text += encrypted_character
# print(encrypted_text)