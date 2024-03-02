words = [word.lower() for word in input().split()]

odd_occurrences = {}

for word in words:
    if word not in odd_occurrences:
        odd_occurrences[word] = 1

    elif word in odd_occurrences:
        odd_occurrences[word] += 1

for word in odd_occurrences:
    if odd_occurrences[word] % 2 != 0:
        print(f"{word}", end=" ")

""" I.S."""

# words = input().split()
# odd_occurrences = {}
#
# for word in words:
#     word = word.lower()
#     if word not in odd_occurrences.keys():
#         odd_occurrences[word] = 1
#     else:
#         odd_occurrences[word] += 1
# for key, value in odd_occurrences.items():
#     if value % 2 != 0:
#         print(f"{key} ", end="")
