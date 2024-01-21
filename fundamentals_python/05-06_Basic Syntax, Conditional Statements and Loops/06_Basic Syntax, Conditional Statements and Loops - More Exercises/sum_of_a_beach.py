input_str = input()

words_to_count = ["Sand", "Water", "Fish", "Sun"]
count = 0
input_str_lower = input_str.lower()

for word in words_to_count:
    count += input_str_lower.count(word.lower())

print(count)


""" from CEO """

text = input().lower()
words = ["sand", "water", "fish", "sun"]
print(sum([text.count(word) for word in words]))