starter_range = ord(input())
end_range = ord(input())
string = input()
total = 0

for character in string:
    if starter_range < ord(character) < end_range:
        total += ord(character)

print(total)

""" """

start_char, end_char, random_string = input(), input(), input()

show_result = 0
for character in random_string:
    if ord(start_char) < ord(character) < ord(end_char):
        show_result += ord(character)

print(show_result)

""" """

start_char, end_char, random_string = input(), input(), input()

print(sum([ord(char) for char in random_string if ord(start_char) < ord(char) < ord(end_char)]))

""" """
