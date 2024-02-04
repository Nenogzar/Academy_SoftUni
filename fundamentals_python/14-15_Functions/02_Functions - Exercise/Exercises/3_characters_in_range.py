start_char = ord(input())
end_char = ord(input())
char_string = [chr(ch) for ch in range(start_char + 1, end_char)]
# print(char_string)
new_chars = ' '.join(char_string)
print(new_chars)

""" function """


def characters_in_between(char1, char2):
    start = ord(char1)
    end = ord(char2)
    char_list = [chr(i) for i in range(start + 1, end)]
    return ' '.join(char_list)


char1, char2 = input(), input()

result = characters_in_between(char1, char2)
print(result)
