import re

with open("split.txt", "r") as file:
    text = file.read()

pattern = r"(^|(?<=\s))([a-z0-9]+[\.\-\_a-z]*)@([a-z\-]+)(\.[a-z]+)+\b"
matches = re.finditer(pattern, text)

list_with_emails = []
list_with_names = []
for match in matches:
    email = match.group()
    username = match.group(2)
    list_with_names.append(username)
    list_with_emails.append(email)
    start_index = match.start()
    end_index = match.end()

    print(f"Email: {email}")
    print(f"Start Index: {start_index}")
    print(f"End Index: {end_index}")
    print()

print(*list_with_names, sep=", ")
print(*list_with_emails, sep=', ')
