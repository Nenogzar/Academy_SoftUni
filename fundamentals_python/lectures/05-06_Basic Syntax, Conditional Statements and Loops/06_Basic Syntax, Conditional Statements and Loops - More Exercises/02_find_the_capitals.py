""" 1 """
word = input()
indices = [i for i, j in enumerate(word) if j.isupper()]
print(indices)

""" 2"""

indices1 = []
for letter in range(len(word)):
    if word[letter].isupper():
        indices1.append(letter)
print(indices1)

""" 3 """

indices2 = []
for letter in range(len(word)):
    if ord(word[letter]) in range(65, 91): # ASCII largest
        indices2.append(letter)
print(indices2)

""" from CEO  """
text = input()

letter_position = [position for position, letter in enumerate(text) if letter.isupper()]
print(letter_position)


""" from CEO  """
# text = input()
#
# letter_position = list()
#
# for position, letter in enumerate(text):
#     if letter.isupper():
#         letter_position.append(position)
#
# print(letter_position)


""" from CEO  """

# import string
#
# text = input()
#
# capital_letter = string.ascii_uppercase
# letter_position = list()
# position = 0
#
# for letter in text:
#     if letter in capital_letter:
#         letter_position.append(position)
#     position += 1
#
# print(letter_position)