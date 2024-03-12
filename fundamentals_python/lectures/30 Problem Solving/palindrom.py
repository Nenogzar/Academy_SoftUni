from icecream import ic

def is_palindrome(substring):
    return substring == substring[::-1]

def find_longest_palindromic_part(number):
    num_str = str(number)
    longest_palindrome = ""

    for i in range(len(num_str)):
        for j in range(i+1, len(num_str)+1):
            substring = num_str[i:j]
            if is_palindrome(substring) and 1< len(substring) >= len(longest_palindrome):
                longest_palindrome = substring

    return longest_palindrome


numbers = [1232112, 1456541111, 1232321127898721, 12312312345, 612121215, 31233216]


for number in numbers:
    longest_palindrome = find_longest_palindromic_part(number)
    if longest_palindrome:
        print(f"Number {number} has the longest palindromic part: {longest_palindrome}")
    else:
        print(f"Number {number} has no palindromic parts.")



#
#
# """ Намиране на най-дългата дължина от всички съществуващи палиндроми """
# def is_palindrome(substring):
#     # Function to check if a substring is a palindrome
#     return substring == substring[::-1]
#
# def find_longest_palindromic_part(number):
#     # Function to find the longest palindromic part of a number
#     num_str = str(number)
#     palindromic_parts = []
#
#
#     for i in range(len(num_str)):
#         for j in range(i+1, len(num_str)+1):
#             substring = num_str[i:j]
#             if is_palindrome(substring):
#                 palindromic_parts.append(substring)
#
#
#     if not palindromic_parts:
#         return 0
#
#     return max(palindromic_parts, key=len)
#
# # Example data: list of numbers
# numbers = [1232112, 1456541111, 2323278987, 12312312345, 612121215, 31233216]
#
# # Find and display the length of the longest palindromic part
# longest_palindrome_lengths = [len(find_longest_palindromic_part(number)) for number in numbers]
# ic(longest_palindrome_lengths)
# max_length = max(longest_palindrome_lengths)
#
# print(f"Дължината на най-дългия палиндром е: {max_length}")
#
#
