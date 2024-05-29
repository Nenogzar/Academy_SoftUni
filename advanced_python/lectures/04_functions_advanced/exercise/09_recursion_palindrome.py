# 09_recursion_palindrome
#################################### TASK CONDITION ############################
"""
https://judge.softuni.org/Contests/Compete/Index/1839#8
9.	Recursion Palindrome

Write a recursive function called palindrome() that will receive a word and an index (always 0).
Implement the function, so it returns "{word} is a palindrome"
if the word is a palindrome and "{word} is not a palindrome"
if the word is not a palindrome using recursion.
Submit only the function in the judge system.

Examples

Test Code
print(palindrome("abcba", 0))

Output

abcba is a palindrome

print(palindrome("peter", 0))

Output

peter is not a palindrome
"""


##########: variant 1 :##########

def palindrome(word, index):
    if index == len(word) // 2:
        return f"{word} is a palindrome"
    if word[index] != word[-1 - index]:
        return f"{word} is not a palindrome"
    return palindrome(word, index + 1)



##########: variant 2 :##########

def palindrome(word, index, right_index=-1):
    if index == len(word) // 2:
        return f"{word} is a palindrome"

    if word[index] != word[right_index]:
        return f"{word} is not a palindrome"

    return palindrome(word, index + 1, right_index - 1)


##########: variant 3 :##########

def palindrome(word, index):
    if word == word[::-1]:
        return f"{word} is a palindrome"
    return f"{word} is not a palindrome"