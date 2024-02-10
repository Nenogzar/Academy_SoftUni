""" 1 """
words = input().split()


def even_length(text):
    for word in text:
        if len(word) % 2 == 0:
            print(word)


even_length(words)

""" 2 """

word_input = input().split(" ")
word_filter = [word for word in word_input if len(word) % 2 == 0]
""" print to new line whit for loop"""
# for w in word_filter:
#     print(w)
""" print to new line whit join method"""
print("\n".join(word_filter))


""" 3 """

[print(text) for text in input().split() if len(text) % 2 == 0]

