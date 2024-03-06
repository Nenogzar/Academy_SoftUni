# txt = input().split(" ")
# for word in txt:
#     txt = word * len(word)
#     print(txt)


# txt = input().split(" ")
# new_txt = ""
#
# for word in txt:
#     len_txt = len(word)
#     new_txt = word * len(word)
#
# print(txt)


txt = input().split()
str_txt = [word * len(word) for word in txt]
print(''.join(str_txt))