def positive_numbers(positive):
    positive_num = [pos for pos in positive if pos >= 0]
    return positive_num


def negative_numbers(negative):
    negativ_num = [neg for neg in negative if neg < 0]
    return negativ_num


def even_numbers(even):
    even_num = [ev for ev in even if ev % 2 == 0]
    return even_num


def odd_numbers(odd):
    odd_list = [od for od in odd if od % 2 != 0]
    return odd_list


def number_classification(check_list):

    print(f"Positive: {', '.join(map(str, positive_numbers(check_list)))}")
    print(f"Negative: {', '.join(map(str, negative_numbers(check_list)))}")
    print(f"Even: {', '.join(map(str, even_numbers(check_list)))}")
    print(f"Odd: {', '.join(map(str, odd_numbers(check_list)))}")


check_list = list(map(int, input().split(", ")))
number_classification(check_list)


""" 2 """

number_list = [int(n) for n in input().split(", ")]

negative = [number for number in number_list if number < 0]
positive = [number for number in number_list if number >= 0]

odd = [number for number in number_list if number % 2 != 0]
even = [number for number in number_list if number % 2 == 0]

print("Positive:", end=" ")
print(*positive, sep = ", ")
print("Negative:", end=" ")
print(*negative, sep = ", ")
print("Even:", end=" ")
print(*even, sep = ", ")
print("Odd:", end=" ")
print(*odd, sep = ", ")