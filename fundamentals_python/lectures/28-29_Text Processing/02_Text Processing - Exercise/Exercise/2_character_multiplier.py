# from icecream import ic

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

