txt = input()
new_txt = ""

while txt != "end":
    new_txt = ''.join(reversed(txt))
    print(f"{txt} = {new_txt}")
    txt = input()

print(f"{txt} = {new_txt}")
