# def palindrome_func(command):
#     for current_palindrome in command:
#         if current_palindrome == current_palindrome[::-1]:
#             is_palindrome = True
#         else:
#             is_palindrome = False
#         print(is_palindrome)
#
#
# palindrome = input().split(", ")
# palindrome_func(palindrome)



[print(n == n[::-1]) for n in input().split(", ")]