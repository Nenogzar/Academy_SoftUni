"""
Write a program that reads a string from the console and
replaces any sequence of the same letters with a single corresponding letter.
"""
from icecream import  ic
text = input()
new_str = ""
final_str = ""

for char in text:
    if char != new_str:
        final_str += char
        new_str = char

print(final_str)

""" CEO """
main_string = input()


for pos, letter in enumerate(range(len(main_string) - 1), 1):
    if main_string[letter] != main_string[pos]:
        # ic(main_string[letter], main_string[pos])
        print(main_string[letter], end="")  #

print(main_string[-1])
