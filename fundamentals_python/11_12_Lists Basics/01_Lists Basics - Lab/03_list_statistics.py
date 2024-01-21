# On the first line, you will receive a number n. On the following n lines, you will receive integers.
# You should create and print two lists:
# •	One with all the positives (including 0) numbers
# •	One with all the negatives numbers
# Finally, print the following message:
# "Count of positives: {count_positives}"
# "Sum of negatives: {sum_of_negatives}"

positiv_list = []
negativ_list = []

for i in range(int(input())):
    number = int(input())
    positiv_list.append(number) if number >= 0 else negativ_list.append(number)

print(positiv_list)
print(negativ_list)
print(f"Count of positives: {len(positiv_list)}")
print(f"Sum of negatives: {sum(negativ_list)}")

################### FROM  zahariev-webbersof ####################

# n = int(input())
#
# positive_numbers = []
# negative_numbers = []
#
# for _ in range(n):
#     number = int(input())
#
#     if number >= 0:
#         positive_numbers.append(number)
#     else:
#         negative_numbers.append(number)
#
# print(positive_numbers)
# print(negative_numbers)
# print('Count of positives:', len(positive_numbers))
# print('Sum of negatives:', sum(negative_numbers))