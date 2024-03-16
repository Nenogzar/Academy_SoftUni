"""
Write a program that finds how many times a word is used in a string.
The output is a single number indicating the number of times the string contains the word.
Note that letter case does not matter – it is case-insensitive.
"""

import re

info = input()
search_word = input()
pattern = rf"(?i)\b{search_word}\b"
matches = re.findall(pattern, info)
print(len(matches))
