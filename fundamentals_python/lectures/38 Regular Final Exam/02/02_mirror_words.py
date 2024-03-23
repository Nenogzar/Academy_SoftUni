import re

info_string = input()

pattern = re.compile(r'([@|#])(?P<first>[A-Za-z]{3,})\1{2}(?P<second>[A-Za-z]{3,})\1')
matches = pattern.finditer(info_string)
mirrored_words = {
    "mirror words": [],
    "invalid pairs": []
}
for match in matches:
    first = match.group('first')
    second = match.group('second')
    if first[::-1] == second and second[::-1] == first:
        mirrored_words['mirror words'].append(f"{first} <=> {second}")
    else:
        mirrored_words['invalid pairs'].append(f"{first} <=> {second}")

if not mirrored_words['mirror words'] and not mirrored_words['invalid pairs']:
    print(f"No word pairs found!")

if mirrored_words['mirror words'] or mirrored_words['invalid pairs']:
    valid_parts = len(mirrored_words['mirror words']) + len(mirrored_words['invalid pairs'])
    print(f"{valid_parts} word pairs found!")

if not mirrored_words['mirror words']:
    print("No mirror words!")


if mirrored_words['mirror words']:
    print("The mirror words are:")
    print(', '.join(mirrored_words['mirror words']))
