removed_word = input().split(", ")
txt = input()
#
# txt = [txt.replace(word, '*'*len(word)) for word in removed_word]
# print(txt[0])
# print(txt[1])


for word in removed_word:
    while word in txt:
        txt = txt.replace(word,"*"*len(word))
print(txt)

