from icecream import ic

input_str = input().split(" ")
str1, str2 = input_str[0], input_str[1]

# ic(str1, str2)
sum_str1, sum_str2, result = [], [], []
for c in str1:
    char = ord(c)
    sum_str1.append(char)

for c in str2:
    char = ord(c)
    sum_str2.append(char)

# ic(sum_str1)
# ic(sum_str2)


for multi1, multi2 in zip(sum_str1, sum_str2):
    result.append(multi1 * multi2)
# ic(result)

result += sum_str1[len(result):] + sum_str2[len(result):]
# ic(result)

result = sum(result)
# ic(result)
print(result)


""" Ivan Shopov"""

first_string, second_string = input().split()
total_sum = 0
if len(first_string) > len(second_string):
    # Here we have multiplication
    for index in range(len(second_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])
    # Here we are adding the rest of the first string
    for index in range(len(second_string), len(first_string)):
        total_sum += ord(first_string[index])
elif len(second_string) > len(first_string):
    # Here we have multiplication
    for index in range(len(first_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])
    # Here we are adding the rest of the first string
    for index in range(len(first_string), len(second_string)):
        total_sum += ord(second_string[index])
else: # elif len(first_string) == len(second_string)
    # Here we have multiplication
    for index in range(len(second_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])
print(total_sum)

""" CEO """
first_string, second_string = input().split()

first_string = [ord(num) for num in first_string]
second_string = [ord(num) for num in second_string]

ic(first_string, second_string)

first_string_len = len(first_string)
second_string_len = len(second_string)
if first_string_len > second_string_len:
    for _ in range(first_string_len - second_string_len):
        second_string.append(1)
elif first_string_len < second_string_len:
    for _ in range(second_string_len - first_string_len):
        first_string.append(1)
print(sum([first_string[i] * second_string[i] for i in range(len(first_string))]))

""" kumchovalcho """

words = input().split()
first_word = words[0]
second_word = words[1]

total_sum = 0
shorter_word = min(len(first_word), len(second_word))
longer_word = max(len(first_word), len(second_word))

longest_word = ''
if len(first_word) >= len(second_word):
    longest_word = first_word
elif len(second_word) >= len(first_word):
    longest_word = second_word

for pair in range(shorter_word):
    total_sum += ord(first_word[pair]) * ord(second_word[pair])

if first_word != second_word:
    for longer_word_letter in range(shorter_word, longer_word):
        total_sum += ord(longest_word[longer_word_letter])

print(total_sum)