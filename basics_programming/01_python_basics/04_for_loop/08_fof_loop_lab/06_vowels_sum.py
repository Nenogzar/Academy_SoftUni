text = input().lower()
num=0
for char in text:
    if char == "a":
        num += 1
    if char == "e":
        num += 2
    if char == "i":
        num += 3
    if char == "o":
        num += 4
    if char == "u":
        num += 5
print(num)
