"""
Write a program that finds all variable names in each string.
A variable name starts with an underscore ("_") and contains only capital and non-capital letters and digits.
Extract only their names without the underscore. Try to do this only with regular expressions.
The output consists of all variable names extracted and printed on a single line, separated by a comma.
"""

import re

pattern = r"\b_([a-zA-Z0-9]+)\b"
info = input()
matches = re.findall(pattern, info)
print(",".join(matches))

