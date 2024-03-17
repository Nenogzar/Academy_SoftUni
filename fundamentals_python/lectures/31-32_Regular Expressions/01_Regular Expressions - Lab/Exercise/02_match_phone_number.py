import re

main_string = input()

patterns = re.compile(r"\+359([ -])2\1([0-9]{3})\1([0-9]{4})\b")
list_result = list()
result = re.finditer(patterns, main_string)

for show in result:
    list_result.append(show[0])

print(*list_result, sep=", ")