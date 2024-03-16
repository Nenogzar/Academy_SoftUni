import re
"""
Write a program that receives strings on different lines and extracts only the numbers.
Print all extracted numbers on a single line, separated by a single space.
"""

info = input()
pathern = r"\d+"

while info:
    matches = re.findall(pathern, info)
    if matches:
        print(" ".join(matches), end=" ")
    info = input()