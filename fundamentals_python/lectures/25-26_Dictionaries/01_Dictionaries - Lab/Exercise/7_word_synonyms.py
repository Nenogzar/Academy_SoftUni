# number_synonyms = int(input())
# synonym_dict = {}
#
# for _ in range(number_synonyms):
#     word, synonym = input(), input()
#     if word not in synonym_dict:
#         synonym_dict[word] = []
#     synonym_dict[word].append(synonym)
#
# for word in synonym_dict:
#     print(f"{word} - {", ".join(synonym_dict[word])}")

""" """

# number_synonyms = int(input())
# synonyms_dict = {}
#
# for _ in range(number_synonyms):
#     word = input()
#     synonym = input()
#
#     if word in synonyms_dict:
#         synonyms_dict[word].append(synonym)
#     else:
#         synonyms_dict[word] = [synonym]
# # print(synonyms_dict)
# for word, synonyms in synonyms_dict.items():
#     print(f"{word} - {', '.join(synonyms)}")

""" """

#
# count_of_synonyms = int(input())
# synonyms = dict()
#
# for item in range(count_of_synonyms):
#     word, synonym = input(), input()
#
#     synonyms[word] = synonyms.get(word, [])
#     synonyms[word].append(synonym)
#
# [print(f"{word} - {', '.join(synonyms[word])}") for word in synonyms]

""" list """

count_of_synonyms = int(input())
synonyms = dict()
word_list, synonym_list = [], []
for item in range(count_of_synonyms):
    word_list.append(input())
    synonym_list.append(input())

    for word in word_list:
        if word not in synonym_list:
            synonyms[word] = []
    for syn in synonym_list:
        synonyms[word].append(syn)


[print(f"{word} - {', '.join(synonyms[word])}") for word in synonyms]


