txt = input()
d, l, o = "", "", ""

for char in txt:
    if char.isdigit():
        d+=char
    elif char.isalpha():
        l += char
    else:
        o+= char
print(f"{d}\n{l}\n{o}")