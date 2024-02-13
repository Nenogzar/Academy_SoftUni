key = int(input())
line = int(input())

word = list()

for _ in range(line):
    letter = input()
    word.append(chr(ord(letter) + key))

print(*word, sep="")